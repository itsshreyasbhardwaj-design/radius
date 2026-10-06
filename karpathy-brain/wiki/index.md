# Index

Catalog of every page in this wiki. Read this first, then drill in.
Chronology lives in `log.md`. Conventions live in `../CLAUDE.md`.

## Start here

| Page | What it is |
| --- | --- |
| [hot.md](hot.md) | **475 words.** The highest-density answer to "how does he think?". Read this before anything else. |

## Synthesis

| Page | What it is |
| --- | --- |
| [rules.md](rules.md) | The seven rules for how he builds and how he teaches. Each corroborated in ≥2 independent places, each with exact quotes and line-level citations. |
| [principles.md](principles.md) | What he believes: understanding over capability, chosen abstraction, simplicity as a target, problem selection. Weakly-evidenced sections marked `[single-source]`. |
| [methods.md](methods.md) | How he works: how he starts a problem, how he moves, how he debugs, how he reads others' results, how he teaches. |

## Sources — one page per raw source

| Page | Files | Words | State |
| --- | ---: | ---: | --- |
| [sources/blog.md](sources/blog.md) | 179 | 110,657 | 23 posts, 2011→2026. Densest written thinking. Skewed pre-2021. |
| [sources/github.md](sources/github.md) | 3,587 | 4,796,444 | 45 repos. **Only ~15% is his** — read the provenance section before using any number. |
| [sources/gist.md](sources/gist.md) | 1 | 1,959 | The LLM Wiki gist — the framework this wiki implements. |
| [sources/youtube.md](sources/youtube.md) | 0 | 0 | **Empty.** Host blocked. No lecture transcripts exist in this corpus. |
| [sources/x.md](sources/x.md) | 0 | 0 | **Empty.** No credential and host blocked. |

Totals: **3,767 files · 4,909,060 words · 174 recorded failures.**

## Machinery

| Path | What it does |
| --- | --- |
| `../CLAUDE.md` | The schema. Conventions, the four standing rules, operations, standing caveats. |
| `../tools/build_manifest.py` | Builds a source manifest (path, bytes, word count, sha256, binary flag, failures). |
| `../tools/verify_quotes.py` | Checks every mined quote verbatim against raw. **160/160 verified, 0 rejected.** |
| `../tools/annotate_github_provenance.py` | Measures fork/dataset share of the github source. |
| `_build/quotes_verified.json` | The 160 verified quotes, with file and line. The evidence base for every page above. |
| `_build/quotes_rejected.json` | Quotes that failed verification. Currently empty. |

## Consumers of this wiki

| Path | What it does |
| --- | --- |
| `../../.claude/agents/karpathy.md` | Subagent that works to the seven rules and cites this wiki. |
| `../../.claude/skills/karpathy-teach/SKILL.md` | Skill that routes a task to that agent and grades the answer against the seven rules. |
| `../../.claude/hooks/karpathy_run_gate.py` | Stop hook: blocks a Karpathy-flavoured turn that wrote code and never ran it. |

## Standing caveats

Every synthesis page restates these, because they bound every claim:

- **No lectures** (YouTube blocked) — so no rule is corroborated by spoken teaching.
- **No X posts** (blocked, no credential) — no coverage of his informal/recent voice.
- **Blog skews pre-2021** (bearblog and Medium blocked) — Software 2.0 is absent.
- **GitHub word counts mislead** — ~66% forks, ~18% vendored data, ~15% his.
- **Repo list is guess-verified**, not authoritative (GitHub listing API blocked).
