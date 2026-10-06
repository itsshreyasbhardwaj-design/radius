#!/usr/bin/env python3
"""Build a manifest for one source subfolder of karpathy-brain/raw.

Every source agent runs this so all manifests share one schema.

Usage:
    python3 -I build_manifest.py <source_dir> <source_name>

Reads, if present:
    <source_dir>/_crawl/failures.json   list of {"target","reason","error"}
    <source_dir>/_crawl/meta.json       free-form dict describing method/limits

Writes:
    <source_dir>/manifest.json
    <source_dir>/MANIFEST.md
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import sys

# Files the manifest describes but never describes itself.
SELF = {"manifest.json", "MANIFEST.md"}
# Crawl bookkeeping lives here and is reported separately, not as corpus files.
CRAWL_DIR = "_crawl"


def is_binary(path: str) -> bool:
    with open(path, "rb") as fh:
        return b"\x00" in fh.read(8192)


def describe(path: str, root: str) -> dict:
    rel = os.path.relpath(path, root)
    size = os.path.getsize(path)
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)

    binary = is_binary(path)
    words = None
    if not binary:
        with open(path, "rb") as fh:
            words = len(fh.read().decode("utf-8", errors="replace").split())

    return {
        "path": rel.replace(os.sep, "/"),
        "bytes": size,
        "word_count": words,
        "binary": binary,
        "sha256": digest.hexdigest(),
    }


def load_json(path: str, fallback):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return fallback


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2

    root, source_name = os.path.abspath(sys.argv[1]), sys.argv[2]
    if not os.path.isdir(root):
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in {".git", CRAWL_DIR})
        for name in sorted(filenames):
            if dirpath == root and name in SELF:
                continue
            full = os.path.join(dirpath, name)
            if os.path.islink(full) or not os.path.isfile(full):
                continue
            files.append(describe(full, root))

    files.sort(key=lambda f: f["path"])
    failures = load_json(os.path.join(root, CRAWL_DIR, "failures.json"), [])
    meta = load_json(os.path.join(root, CRAWL_DIR, "meta.json"), {})

    text_files = [f for f in files if not f["binary"]]
    manifest = {
        "source": source_name,
        "generated_at_utc": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "collection": meta,
        "counts": {
            "files": len(files),
            "text_files": len(text_files),
            "binary_files": len(files) - len(text_files),
            "total_bytes": sum(f["bytes"] for f in files),
            "total_words": sum(f["word_count"] or 0 for f in text_files),
            "failures": len(failures),
        },
        "files": files,
        "failures": failures,
    }

    with open(os.path.join(root, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    counts = manifest["counts"]
    lines = [
        f"# Manifest — `{source_name}`",
        "",
        f"Generated: {manifest['generated_at_utc']}",
        "",
        f"- Files: **{counts['files']}** ({counts['text_files']} text, "
        f"{counts['binary_files']} binary)",
        f"- Total words: **{counts['total_words']:,}**",
        f"- Total bytes: **{counts['total_bytes']:,}**",
        f"- Failures: **{counts['failures']}**",
        "",
    ]

    if meta:
        lines += ["## Collection method", "", "```json",
                  json.dumps(meta, indent=2, ensure_ascii=False), "```", ""]

    lines += ["## Files", "", "| File | Words | Bytes |", "| --- | ---: | ---: |"]
    for f in files:
        words = "—" if f["word_count"] is None else f"{f['word_count']:,}"
        lines.append(f"| `{f['path']}` | {words} | {f['bytes']:,} |")
    lines.append("")

    lines += ["## Failures", ""]
    if failures:
        lines += ["| Target | Reason | Error |", "| --- | --- | --- |"]
        for item in failures:
            target = str(item.get("target", "")).replace("|", "\\|")
            reason = str(item.get("reason", "")).replace("|", "\\|")
            error = str(item.get("error", "")).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| `{target}` | {reason} | {error} |")
    else:
        lines.append("None.")
    lines.append("")

    with open(os.path.join(root, "MANIFEST.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
