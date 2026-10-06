#!/usr/bin/env python3
"""Verify every mined quote appears verbatim in the raw corpus.

The wiki's rule is that every claim about Karpathy carries a quote from raw.
That rule is only worth anything if the quotes are real, so nothing reaches
the wiki until it has survived this check: the quote string must appear
character-for-character in the file it cites.

Notebooks are handled specially — a quote lives in a markdown cell, and the
.ipynb on disk stores that cell JSON-escaped, so the cell sources are decoded
before matching.

Usage:
    python3 -I verify_quotes.py <wiki_dir> <raw_dir>

Reads  <wiki_dir>/_build/quotes_*.json
Writes <wiki_dir>/_build/quotes_verified.json
       <wiki_dir>/_build/quotes_rejected.json
"""

from __future__ import annotations

import glob
import json
import os
import sys

REQUIRED = {"quote", "file", "theme", "note"}


def notebook_text(path: str) -> str:
    """Concatenate decoded cell sources so quotes match what a reader sees."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            nb = json.load(fh)
    except (OSError, ValueError):
        return ""
    chunks = []
    for cell in nb.get("cells", []):
        src = cell.get("source", "")
        chunks.append("".join(src) if isinstance(src, list) else str(src))
    return "\n".join(chunks)


def load_text(path: str, cache: dict) -> str:
    if path not in cache:
        if path.endswith(".ipynb"):
            cache[path] = notebook_text(path)
        else:
            try:
                with open(path, encoding="utf-8", errors="replace") as fh:
                    cache[path] = fh.read()
            except OSError:
                cache[path] = ""
    return cache[path]


def line_of(text: str, quote: str) -> int | None:
    idx = text.find(quote)
    return None if idx < 0 else text.count("\n", 0, idx) + 1


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    wiki, raw = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    build = os.path.join(wiki, "_build")

    verified, rejected, cache, seen = [], [], {}, set()

    for src in sorted(glob.glob(os.path.join(build, "quotes_*.json"))):
        base = os.path.basename(src)
        if base in {"quotes_verified.json", "quotes_rejected.json"}:
            continue
        try:
            with open(src, encoding="utf-8") as fh:
                items = json.load(fh)
        except (OSError, ValueError) as exc:
            rejected.append({"quote": "", "file": base, "reason": f"unreadable inventory: {exc}"})
            continue

        for item in items if isinstance(items, list) else []:
            if not isinstance(item, dict) or not REQUIRED <= set(item):
                rejected.append({"quote": str(item)[:120], "file": base,
                                 "reason": "missing required keys"})
                continue

            quote, rel = item["quote"], item["file"].lstrip("/")
            full = os.path.join(raw, rel)

            if not quote.strip():
                rejected.append({**item, "reason": "empty quote"})
                continue
            if not os.path.isfile(full):
                rejected.append({**item, "reason": "cited file does not exist"})
                continue

            text = load_text(full, cache)
            if quote not in text:
                rejected.append({**item, "reason": "quote not found verbatim in cited file"})
                continue

            key = (quote.strip(), rel)
            if key in seen:
                rejected.append({**item, "reason": "duplicate of an already-verified quote"})
                continue
            seen.add(key)

            verified.append({**item, "line": line_of(text, quote), "inventory": base})

    for name, payload in (("quotes_verified.json", verified),
                          ("quotes_rejected.json", rejected)):
        with open(os.path.join(build, name), "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False)
            fh.write("\n")

    by_source = {}
    for q in verified:
        by_source[q["file"].split("/")[0]] = by_source.get(q["file"].split("/")[0], 0) + 1
    by_theme = {}
    for q in verified:
        by_theme[q["theme"]] = by_theme.get(q["theme"], 0) + 1

    print(json.dumps({
        "verified": len(verified),
        "rejected": len(rejected),
        "distinct_files": len({q["file"] for q in verified}),
        "by_source": by_source,
        "by_theme": dict(sorted(by_theme.items(), key=lambda kv: -kv[1])),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
