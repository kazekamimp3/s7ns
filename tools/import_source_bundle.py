#!/usr/bin/env python3
"""
Import the bundled S7NS source archive into kazekamimp3/s7ns.

Requirements:
  - Python 3.9+
  - A GitHub fine-grained PAT with Contents: Read and write on kazekamimp3/s7ns
  - Set GITHUB_TOKEN (or GH_TOKEN) in the environment

Usage:
  python tools/import_source_bundle.py S7NS_SOURCE_BUNDLE.zip

The script creates one Git commit, updates main without force-pushing, then
checks every raw GitHub URL against the bundled SHA-256 manifest.
"""
import base64
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPO = os.environ.get("GITHUB_REPO", "kazekamimp3/s7ns")
API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
USER_AGENT = "S7NS-Source-Archive-Importer/1.0"

def request(method, url, payload=None, raw=False):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            body = response.read()
            return body if raw else json.loads(body.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"GitHub API {method} {url} failed: HTTP {exc.code}: {detail}") from exc

def api(method, path, payload=None):
    return request(method, API + path, payload)

def main():
    if not TOKEN:
        raise SystemExit("Set GITHUB_TOKEN or GH_TOKEN to a fine-grained token with Contents: Read and write.")
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python tools/import_source_bundle.py S7NS_SOURCE_BUNDLE.zip")
    bundle_path = sys.argv[1]

    with zipfile.ZipFile(bundle_path, "r") as zf:
        names = set(zf.namelist())
        manifest_name = "SOURCE_MANIFEST.json"
        if manifest_name not in names:
            raise SystemExit("Bundle is missing SOURCE_MANIFEST.json.")
        manifest = json.loads(zf.read(manifest_name).decode("utf-8"))
        files = manifest["files"]
        if len(files) != manifest["source_file_count"]:
            raise SystemExit("Manifest file count mismatch.")
        upload_items = []
        for item in files:
            path = item["repository_path"]
            data = zf.read(path)
            if len(data) != item["size_bytes"]:
                raise SystemExit(f"Size mismatch before upload: {path}")
            digest = hashlib.sha256(data).hexdigest()
            if digest != item["sha256"]:
                raise SystemExit(f"SHA-256 mismatch before upload: {path}")
            upload_items.append((path, data))

        # Generated navigation files are uploaded alongside the original owners.
        for path in ("README.md", "S7NS_SOURCE_INDEX.md", "AI_STUDIO_SOURCE_ACCESS.md", "SOURCE_MANIFEST.json"):
            upload_items.append((path, zf.read(path)))
        # Include this importer in the repository for future repeatable imports.
        importer_path = "tools/import_source_bundle.py"
        with open(__file__, "rb") as handle:
            upload_items.append((importer_path, handle.read()))

        repo = api("GET", f"/repos/{REPO}")
        if repo.get("default_branch") != "main":
            raise SystemExit(f"Expected main as default branch; found {repo.get('default_branch')!r}.")
        ref = api("GET", f"/repos/{REPO}/git/ref/heads/main")
        parent_sha = ref["object"]["sha"]
        parent = api("GET", f"/repos/{REPO}/git/commits/{parent_sha}")
        base_tree = parent["tree"]["sha"]

        tree_entries = []
        for index, (path, data) in enumerate(upload_items, 1):
            blob = api("POST", f"/repos/{REPO}/git/blobs", {
                "content": base64.b64encode(data).decode("ascii"),
                "encoding": "base64",
            })
            tree_entries.append({
                "path": path,
                "mode": "100644",
                "type": "blob",
                "sha": blob["sha"],
            })
            print(f"[{index}/{len(upload_items)}] prepared {path}", flush=True)
            time.sleep(0.05)

        tree = api("POST", f"/repos/{REPO}/git/trees", {
            "base_tree": base_tree,
            "tree": tree_entries,
        })
        commit = api("POST", f"/repos/{REPO}/git/commits", {
            "message": "Import complete S7NS source archive and AI Studio raw-link index",
            "tree": tree["sha"],
            "parents": [parent_sha],
        })
        api("PATCH", f"/repos/{REPO}/git/refs/heads/main", {
            "sha": commit["sha"],
            "force": False,
        })

    print(f"\nCommitted: {commit['sha']}")
    print(f"Repository: https://github.com/{REPO}")
    print("Verifying public raw links...")
    failures = []
    for item in files:
        url = f"https://raw.githubusercontent.com/{REPO}/main/{item['repository_path']}"
        try:
            data = request("GET", url, raw=True)
            actual = hashlib.sha256(data).hexdigest()
            if actual != item["sha256"] or len(data) != item["size_bytes"]:
                failures.append((item["repository_path"], "content hash/size mismatch"))
            else:
                print("OK", item["repository_path"])
        except Exception as exc:
            failures.append((item["repository_path"], str(exc)))
    if failures:
        print("\nRAW-LINK VERIFICATION FAILURES:")
        for path, reason in failures:
            print("-", path, reason)
        raise SystemExit(2)
    print(f"\nSUCCESS: all {len(files)} source raw links verified.")
    print(f"Index: https://raw.githubusercontent.com/{REPO}/main/S7NS_SOURCE_INDEX.md")
    print(f"AI Studio guide: https://raw.githubusercontent.com/{REPO}/main/AI_STUDIO_SOURCE_ACCESS.md")

if __name__ == "__main__":
    main()
