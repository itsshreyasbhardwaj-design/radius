#!/usr/bin/env python3
"""Lint the wiki — the health check the LLM Wiki pattern calls for.

Checks the structural promises this wiki makes, so they cannot quietly rot:
every raw source has a page, the hot page stays under its word cap, every
rule is corroborated across at least two distinct files, every quote still
verifies, no page is orphaned from the index, and the agent and skill still
carry the contract they advertise.

Usage:
    python3 -I lint_wiki.py <repo_root>

Exit 0 = clean, 1 = findings.
"""

from __future__ import annotations

import json
import os
import re
import sys

HOT_WORD_CAP = 500


def read(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


def section(text: str, heading: str) -> str:
    """The body under a `## heading`, up to the next `## `."""
    match = re.search(rf"^## {re.escape(heading)}\s*$(.*?)(?=^## |\Z)",
                      text, re.M | re.S)
    return match.group(1) if match else ""


def main() -> int:
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    brain = os.path.join(root, "karpathy-brain")
    wiki = os.path.join(brain, "wiki")
    findings: list[str] = []
    checks = 0

    def check(ok: bool, label: str, detail: str = "") -> None:
        nonlocal checks
        checks += 1
        print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f" — {detail}" if detail else ""))
        if not ok:
            findings.append(f"{label}{' — ' + detail if detail else ''}")

    # --- structure -------------------------------------------------------
    print("== structure ==")
    for name in ("index.md", "log.md", "hot.md", "rules.md",
                 "principles.md", "methods.md"):
        check(os.path.isfile(os.path.join(wiki, name)), f"{name} exists")

    log = read(os.path.join(wiki, "log.md"))
    entries = re.findall(r"^## \[\d{4}-\d\d-\d\d\] \w+ \| ", log, re.M)
    check(bool(entries), "log entries are greppable", f"{len(entries)} entries")

    raw_dir = os.path.join(brain, "raw")
    raw_sources = sorted(d for d in os.listdir(raw_dir)
                         if os.path.isdir(os.path.join(raw_dir, d)))
    pages = sorted(f[:-3] for f in os.listdir(os.path.join(wiki, "sources"))
                   if f.endswith(".md"))
    check(pages == raw_sources, "one page per raw source",
          f"pages={pages} raw={raw_sources}")

    for source in raw_sources:
        manifest = os.path.join(raw_dir, source, "manifest.json")
        check(os.path.isfile(manifest), f"raw/{source} has a manifest")

    # --- hot page cap, under either counting convention ------------------
    print("\n== hot page ==")
    hot = read(os.path.join(wiki, "hot.md"))
    words = len(hot.split())
    check(0 < words < HOT_WORD_CAP, f"hot.md under {HOT_WORD_CAP} words",
          f"{words} words")

    # --- evidence --------------------------------------------------------
    print("\n== evidence ==")
    try:
        verified = json.load(open(os.path.join(wiki, "_build",
                                               "quotes_verified.json"), encoding="utf-8"))
        rejected = json.load(open(os.path.join(wiki, "_build",
                                               "quotes_rejected.json"), encoding="utf-8"))
    except (OSError, ValueError):
        verified, rejected = [], [{"reason": "inventory unreadable"}]
    check(bool(verified), "verified quotes exist", f"{len(verified)} quotes")
    check(not rejected, "no rejected quotes", f"{len(rejected)} rejected")
    check(len({q['file'] for q in verified}) >= 10 if verified else False,
          "quotes span many files",
          f"{len({q['file'] for q in verified})} files" if verified else "none")
    bad = [q for q in verified if q["file"].startswith(("github/transformers/",
                                                        "github/nn/"))]
    check(not bad, "no quotes taken from forked repos", f"{len(bad)} offenders")

    # --- the seven rules -------------------------------------------------
    print("\n== rules.md ==")
    rules = read(os.path.join(wiki, "rules.md"))
    blocks = re.split(r"^## \d+\. ", rules, flags=re.M)[1:]
    check(len(blocks) == 7, "exactly seven rules", f"{len(blocks)} found")
    for i, block in enumerate(blocks, 1):
        quotes = re.findall(r'^> "', block, re.M)
        cites = re.findall(r"^> — `([^:`]+)", block, re.M)
        distinct = set(cites)
        check(len(quotes) >= 2 and len(quotes) == len(cites) and len(distinct) >= 2,
              f"rule {i} corroborated",
              f"{len(quotes)} quotes, {len(cites)} cites, {len(distinct)} distinct files")
    check("[builds]" in rules and "[teaches]" in rules,
          "rules cover building and teaching")

    # --- consumers honour their contract ---------------------------------
    print("\n== agent + skill ==")
    agent = read(os.path.join(root, ".claude", "agents", "karpathy.md"))
    check("name: karpathy" in agent, "agent is named karpathy")
    check("hot.md` first" in agent, "agent reads the hot page first")
    check("at most five wiki pages" in agent, "agent caps wiki reads at five")
    seven = re.findall(r"^\d+\. \*\*", section(agent, "The seven rules — follow every one, on every task"), re.M)
    check(len(seven) == 7, "agent embeds all seven rules", f"{len(seven)} found")
    check("must cite the wiki page" in agent, "agent must cite the wiki")
    check(all(k in agent for k in ("Ran:", "Output:", "Changed:")),
          "agent ends with ran / output / changed")

    skill = read(os.path.join(root, ".claude", "skills", "karpathy-teach", "SKILL.md"))
    check("name: karpathy-teach" in skill, "skill is named karpathy-teach")
    check("karpathy` subagent" in skill, "skill hands the task to the agent")
    check("grade" in skill.lower(), "skill grades the answer")

    # --- orphans ---------------------------------------------------------
    print("\n== orphans ==")
    index = read(os.path.join(wiki, "index.md"))
    orphans = []
    for dirpath, dirnames, filenames in os.walk(wiki):
        dirnames[:] = [d for d in dirnames if d != "_build"]
        for name in filenames:
            if not name.endswith(".md") or name == "index.md":
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), wiki).replace(os.sep, "/")
            if rel not in index:
                orphans.append(rel)
    check(not orphans, "every page is linked from the index", ", ".join(orphans))

    print()
    if findings:
        print(f"{len(findings)} finding(s) out of {checks} checks")
        return 1
    print(f"clean — {checks} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
