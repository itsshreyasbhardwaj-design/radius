# Source — gist

**Raw path:** `raw/gist/` · **Manifest:** `raw/gist/manifest.json`
**1 file · 1,959 words · 1 failure**

## What it holds

`llm-wiki.md` — Karpathy's "LLM Wiki" gist, which is **the framework this entire
wiki is built on**. It describes a pattern for building personal knowledge bases
with LLMs: three layers (immutable raw sources, an LLM-written wiki, a schema
file), three operations (ingest, query, lint), and two special files (`index.md`
for content, `log.md` for chronology).

Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## How it was collected

Cloned over the git protocol:

```
git clone https://gist.github.com/442a6bf555914893e9891c11519de94f
```

`gist.github.com` is reachable over git in this environment even though the
GitHub web and API hosts are blocked — the same quirk that made the blog and repo
sources possible.

## Why it is filed in `raw/`

It was supplied directly as the framework rather than discovered by a crawl, but
it is Karpathy's own public writing, so it belongs in the corpus as a source in
its own right rather than sitting loose outside it. It is quotable like any other
source, and `karpathy-brain/CLAUDE.md` implements the pattern it describes.

Adding it touched no existing raw file — new source folder, own `_crawl/`
bookkeeping, own manifest. The immutability rule is intact.

## What is missing

**This is one gist — the one supplied.** Karpathy has other public gists that are
not collected here, and this crawl cannot enumerate them: listing gists by user
requires the GitHub API, which is blocked for this session.
