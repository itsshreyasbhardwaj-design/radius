# Log

Append-only chronology. Newest at the bottom. Entry format is fixed so the log
stays greppable:

```
## [YYYY-MM-DD] <op> | <title>
```

Ops: `ingest`, `query`, `lint`, `build`.

```
grep "^## \[" log.md | tail -5
```

---

## [2026-10-06] ingest | blog — karpathy.github.io + paper-notes

179 files, 110,657 words, 10 failures. Cloned the Jekyll source rather than
scraping; the rendered site is blocked but the repo carries every post as raw
markdown with front matter intact. 23 posts, 2011-04-27 → 2026-02-12.
Failures recorded: bearblog.dev and Medium blocked, seven candidate writing repos
did not resolve. Created `sources/blog.md`.

## [2026-10-06] ingest | github — 45 repos

3,587 files, 4,796,444 words, 155 failures. `git clone --depth 1` per repo, `.git`
stripped. Repo list is guess-verified: the GitHub user-listing API is blocked, so
203 candidate names were checked with `git ls-remote` and the 46 that resolved
were taken. Created `sources/github.md`.

## [2026-10-06] ingest | youtube — FAILED, zero files

`yt-dlp` 2026.08.19 and `youtube-transcript-api` both installed cleanly from PyPI,
but every request to youtube.com was refused at the proxy CONNECT layer with 403.
Captured stderr kept under `raw/youtube/_crawl/` as evidence. Created
`sources/youtube.md`. **Consequence for the wiki: no rule can be corroborated by a
lecture.**

## [2026-10-06] ingest | x — FAILED, zero files

Two independent blockers: no `.env` file exists anywhere in this environment, and
api.twitterapi.io is blocked. No credential value was requested or stored.
Created `sources/x.md`.

## [2026-10-06] build | provenance measurement of the github source

Measured what the 4.8M words actually are. 66.3% is forks of other people's
projects (`transformers` is 64.8% on its own; `nn` is a fork of torch/nn), 18.4%
is vendored datasets and lockfiles (tinyshakespeare appears three times), leaving
~15.3% plausibly Karpathy-authored. Nothing deleted — recorded in
`raw/github/_crawl/provenance.json` so filtering happens at the point of use.
Added `tools/annotate_github_provenance.py`.

## [2026-10-06] ingest | gist — llm-wiki.md

1 file, 1,959 words. Cloned over git from gist.github.com, which is reachable even
though the GitHub web and API hosts are not. This is the framework the wiki
implements. Filed as a raw source in its own right; no existing raw file was
touched. Created `sources/gist.md` and the schema at `../CLAUDE.md`.

## [2026-10-06] build | quote mining and verification

Mined 160 candidate quotes (77 blog, 83 github) across 62 distinct files, then
verified every one character-for-character against the cited raw file with
`tools/verify_quotes.py`. **160 verified, 0 rejected.** Forks (`transformers/`,
`nn/`) and vendored data were excluded from mining. Evidence base written to
`_build/quotes_verified.json`.

## [2026-10-06] build | synthesis pages

Wrote `rules.md` (seven rules, each corroborated in ≥2 independent places),
`principles.md`, `methods.md`, and `hot.md` (475 words, under the 500 cap).
Created `index.md`.

Recorded honestly on `rules.md`: the corroboration test is weaker than intended
because the second source is never a lecture — only 1 of 7 rules is a teaching
rule, and that is a floor set by the evidence, not a claim about him.

## [2026-10-06] build | consumers — agent, skill, run gate

Turned the seven rules into `.claude/agents/karpathy.md` (reads `hot.md` first,
caps at five wiki pages, cites the wiki, ends with ran/output/changed),
`.claude/skills/karpathy-teach/SKILL.md` (routes a task to that agent and grades
the answer against the seven rules before showing it), and
`.claude/hooks/karpathy_run_gate.py` (Stop hook that blocks a Karpathy-flavoured
turn which wrote code and never ran it).
