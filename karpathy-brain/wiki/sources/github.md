# Source — github

**Raw path:** `raw/github/` · **Manifest:** `raw/github/manifest.json`
**3,587 files · 4,796,444 words · 155 failures · 45 repos**

The largest source by volume and the most misleading one. Read the provenance
section before using any number from it.

## The provenance problem

Being in his account is not the same as being written by him. Measured in
`raw/github/_crawl/provenance.json`:

| Share | What it is |
| ---: | --- |
| **66.3%** | Forks of other people's projects — `transformers/` is a fork of huggingface/transformers and is 64.8% of this source alone; `nn/` is a fork of torch/nn |
| **18.4%** | Vendored datasets, fixtures and lockfiles — the tinyshakespeare corpus appears **three times** (`build-nanogpt`, `char-rnn`, `ng-video-lecture`), plus a names dataset, a tokenizer test fixture, a uv lockfile |
| **~15.3%** | Plausibly Karpathy-authored |

**Never quote from `transformers/` or `nn/`.** Anything weighting this source by
raw word count is learning HuggingFace and Torch, not Karpathy.

Fork status was established by reading each repo's own README and LICENSE,
because the GitHub API that reports fork status is blocked here.

## The 45 repos

```
EigenLibSVM          cryptos                 minGPT            pytorch-made
Random-Forest-Matlab deep-vector-quantization minbpe           pytorch-normalizing-flows
arxiv-sanity-lite    find-birds              nanoGPT           randomfun
arxiv-sanity-preserver forestjs              nanochat          recurrentjs
build-nanogpt        gitstats                neuraltalk        reinforcejs
char-rnn             karpathy  (profile)     neuraltalk2       researchlei
convnetjs            lecun1989-repro         ng-video-lecture  researchpooler
covid-sanity         llama2.c                nipspreview       scholaroctopus
llm-council          llm.c                   nn      (fork)    svmjs
llm101n              makemore                nn-zero-to-hero   tf-agent
                     micrograd               paper-notes       transformers (fork)
                                                               tsnejs
                                                               ulogme
```

Highest-yield for this wiki: `micrograd`, `minGPT`, `nanoGPT`, `nanochat`,
`llm.c`, `llama2.c`, `minbpe`, `makemore`, `nn-zero-to-hero`, `llm101n` — the
teaching-oriented from-scratch implementations where he states intent in the
README.

## How it was collected

`git clone --depth 1 --single-branch` per repo, `.git` stripped afterwards.
Files kept exactly as they came down. 95 MB on disk.

## What is missing — read before drawing conclusions

**The repo list is guess-verified, not authoritative.** The GitHub user-listing
API, the plain `github.com/karpathy` web page, `codeload`, and third-party
mirrors are all blocked for this session. There was no way to obtain a real
listing. Instead a 203-name candidate list was assembled and every name checked
with `git ls-remote`; the 46 that resolved were taken (`karpathy.github.io`
delegated to the blog source).

Any public repo whose name was not guessed is **silently absent, and this crawl
cannot tell how many such repos exist.** The 155 non-resolving candidates are
listed in `raw/github/_crawl/failures.json`.

One further limit: `git ls-remote` answers identically for a nonexistent repo and
a private one, so "did not resolve" cannot distinguish the two.
