# karpathy-brain — wiki schema

This is the schema layer described in Karpathy's LLM Wiki pattern
(`raw/gist/llm-wiki.md`). It tells an agent how this wiki is structured and how
to work on it. Read this before touching anything in `karpathy-brain/`.

## Three layers

| Layer | Path | Who owns it |
| --- | --- | --- |
| Raw sources | `raw/` | **Immutable.** Read-only, always. |
| The wiki | `wiki/` | The agent writes and maintains all of it. |
| The schema | this file | Co-evolved by human and agent. |

### Rule 1 — `raw/` is immutable

Never edit, reformat, move, rename or delete anything under `raw/`. Not to fix a
typo, not to normalize whitespace, not to strip a stray file. Sources may be
**added** (a new source gets its own subfolder, its own `_crawl/` bookkeeping and
its own manifest), but existing bytes are never touched. Every manifest records
sha256 per file, so edits are detectable.

### Rule 2 — every claim about Karpathy carries a quote

Any sentence in the wiki asserting what he believes, does, or recommends must be
backed by a verbatim quote from `raw/`, with the source file cited. No quote, no
claim. Statements about the *corpus itself* (file counts, what is missing, how it
was collected) are exempt — those cite the manifests.

### Rule 3 — quotes are verified, not trusted

Quotes are mined into `wiki/_build/quotes_*.json`, then checked
character-for-character against the cited raw file:

```
python3 -I tools/verify_quotes.py wiki raw
```

This writes `wiki/_build/quotes_verified.json` and `quotes_rejected.json`. Only
verified quotes may be used. A quote that cannot be found verbatim is dropped,
never "fixed".

### Rule 4 — a rule needs two independent sources

Pages that assert a durable pattern (`rules.md`, `principles.md`, `methods.md`)
only keep a claim if it appears in **at least two different places** — two
different posts, or a post and a repo. Single-source observations are interesting
but go in a source page, not a rules page.

## Page inventory

| Page | Purpose |
| --- | --- |
| `wiki/index.md` | Content catalog. Every page, one line each. Read this first. |
| `wiki/log.md` | Append-only chronology. Entries start `## [YYYY-MM-DD] <op> \| <title>`. |
| `wiki/hot.md` | Under 500 words. The highest-density answer to "how does he think?". |
| `wiki/rules.md` | The seven corroborated rules, each with quote + sources. |
| `wiki/principles.md` | What he believes. |
| `wiki/methods.md` | How he works and teaches. |
| `wiki/sources/<source>.md` | One page per raw source: what it holds, what it misses. |

## Operations

**Ingest.** Add the source under `raw/<name>/` with `_crawl/meta.json` and
`_crawl/failures.json`, build its manifest, mine quotes, verify them, update the
affected wiki pages, update `index.md`, append to `log.md`.

**Query.** Read `index.md`, then `hot.md`, then at most a few specific pages.
Answers worth keeping get filed back as new wiki pages.

**Lint.** Check for: claims without quotes, quotes that no longer verify, pages
not listed in `index.md`, rules resting on only one source, and stale coverage
caveats.

```
python3 -I tools/build_manifest.py raw/<source> <source>   # rebuild a manifest
python3 -I tools/verify_quotes.py wiki raw                 # re-verify all quotes
python3 -I tools/annotate_github_provenance.py raw/github  # re-measure authorship
grep "^## \[" wiki/log.md | tail -5                        # recent activity
```

## Standing caveats the wiki must keep repeating

These shape every conclusion drawn here, so pages that synthesize must restate
them rather than quietly assuming full coverage:

- **No lectures.** The YouTube source is empty — the host was blocked. His spoken
  teaching, which is a large part of his public output, is absent.
- **No X posts.** Empty for the same reason, plus no credential.
- **Blog is skewed pre-2021.** `karpathy.bearblog.dev` is blocked, so his recent
  writing is largely missing.
- **GitHub word counts mislead.** ~66% of that source is forks of other people's
  projects and ~18% is vendored datasets; only ~15% is plausibly his. See
  `raw/github/_crawl/provenance.json`. Never quote from `transformers/` or `nn/`.
- **The repo list is guess-verified**, not authoritative — the GitHub listing API
  is blocked.
