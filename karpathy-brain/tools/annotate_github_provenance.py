#!/usr/bin/env python3
"""Annotate the github source with provenance facts.

The crawl collects every repo under github.com/karpathy, but "in his account"
is not the same as "written by him". Forks and vendored datasets dominate the
raw word count, so anything downstream that weights by volume would be
learning mostly third-party code. This script measures that and records it;
it deletes nothing.

Usage:
    python3 -I annotate_github_provenance.py <github_source_dir>
"""

from __future__ import annotations

import collections
import json
import os
import sys

# Repos that live in his account but are forks of other projects. Established
# by reading each repo's own README/LICENSE, since the GitHub API (which would
# report fork status directly) is blocked in this environment.
FORKS = {
    "transformers": "fork of huggingface/transformers (README is "
                    "'Copyright 2020 The HuggingFace Team')",
    "nn": "fork of torch/nn (README carries the torch/nn Travis badge)",
}

# Files that are datasets, fixtures, lockfiles or generated blobs rather than
# authored prose or code. Matched by exact relative path.
NON_AUTHORED = {
    "build-nanogpt/input.txt": "tinyshakespeare training corpus",
    "char-rnn/data/tinyshakespeare/input.txt": "tinyshakespeare training corpus",
    "ng-video-lecture/input.txt": "tinyshakespeare training corpus",
    "scholaroctopus/render/data5.json": "scraped paper metadata",
    "makemore/names.txt": "names dataset",
    "minbpe/tests/taylorswift.txt": "tokenizer test fixture",
    "nanochat/uv.lock": "generated dependency lockfile",
}


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    root = os.path.abspath(sys.argv[1])

    with open(os.path.join(root, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)

    per_repo = collections.Counter()
    for entry in manifest["files"]:
        per_repo[entry["path"].split("/")[0]] += entry["word_count"] or 0
    total = sum(per_repo.values())

    fork_words = sum(per_repo[r] for r in FORKS if r in per_repo)
    data_words = sum(
        e["word_count"] or 0
        for e in manifest["files"]
        if e["path"] in NON_AUTHORED
    )
    authored = total - fork_words - data_words

    def pct(n: int) -> float:
        return round(100.0 * n / total, 1) if total else 0.0

    provenance = {
        "why_this_exists": "Repo count is a poor proxy for authorship. Two "
                           "forks and a handful of vendored datasets carry "
                           "most of the words in this source, so any "
                           "downstream process that weights by volume would "
                           "be dominated by code and text Karpathy did not "
                           "write.",
        "method": "Fork status was established by reading each repo's own "
                  "README and LICENSE, because the GitHub API that reports "
                  "fork status is blocked in this environment. Word counts "
                  "come from the manifest.",
        "totals": {
            "all_words": total,
            "third_party_fork_words": fork_words,
            "third_party_fork_pct": pct(fork_words),
            "vendored_dataset_words": data_words,
            "vendored_dataset_pct": pct(data_words),
            "plausibly_authored_words": authored,
            "plausibly_authored_pct": pct(authored),
        },
        "third_party_forks": [
            {"repo": r, "words": per_repo.get(r, 0),
             "pct_of_source": pct(per_repo.get(r, 0)), "evidence": why}
            for r, why in sorted(FORKS.items(), key=lambda kv: -per_repo.get(kv[0], 0))
        ],
        "vendored_or_generated_files": [
            {"path": p, "words": next(
                (e["word_count"] or 0 for e in manifest["files"]
                 if e["path"] == p), 0), "kind": kind}
            for p, kind in sorted(
                NON_AUTHORED.items(),
                key=lambda kv: -next(
                    (e["word_count"] or 0 for e in manifest["files"]
                     if e["path"] == kv[0]), 0))
        ],
        "guidance": "Nothing was deleted — this source is raw by design. "
                    "Filter on these paths at the point of use rather than "
                    "trusting the headline word count.",
        "repo_word_counts": dict(per_repo.most_common()),
    }

    out = os.path.join(root, "_crawl", "provenance.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(provenance, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    meta_path = os.path.join(root, "_crawl", "meta.json")
    with open(meta_path, encoding="utf-8") as fh:
        meta = json.load(fh)
    meta["provenance_warning"] = {
        "summary": f"{pct(fork_words)}% of this source's words come from two "
                   f"forks of other people's projects (transformers, nn), and "
                   f"a further {pct(data_words)}% are vendored datasets and "
                   f"lockfiles. Only about {pct(authored)}% is plausibly "
                   f"Karpathy-authored. Do not weight by raw word count.",
        "detail_file": "_crawl/provenance.json",
    }
    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(json.dumps(provenance["totals"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
