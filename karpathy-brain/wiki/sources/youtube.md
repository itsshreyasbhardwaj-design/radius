# Source — youtube

**Raw path:** `raw/youtube/` · **Manifest:** `raw/youtube/manifest.json`
**0 files · 0 words · 4 failures — THIS SOURCE IS EMPTY**

## What was intended

Enumerate the `@AndrejKarpathy` channel with `yt-dlp`, then pull caption
transcripts for every lecture with `youtube-transcript-api`, falling back to
`yt-dlp` for auto-generated captions.

## What happened

Both tools installed cleanly — PyPI is reachable. `yt-dlp` 2026.08.19 and
`youtube-transcript-api` are present and working. **Every request to YouTube was
refused at the proxy CONNECT layer with 403 Forbidden.**

```
ERROR: [youtube:tab] @AndrejKarpathy/videos: Unable to download API page:
  ('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden'))

ProxyError: HTTPSConnectionPool(host='www.youtube.com', port=443):
  Max retries exceeded with url: /watch?v=kCc8FmEb1nY
```

Captured stderr is kept verbatim in `raw/youtube/_crawl/` as evidence. This is a
network-policy denial, not a tool, version, or rate-limit problem — so it is
fixable by configuration, and the source becomes a re-run rather than a rebuild.

## Why this gap matters more than its file count suggests

His lectures are a large fraction of his public teaching output, and they are
where he *explains his reasoning aloud* rather than stating conclusions. The
"Zero to Hero" series, "Let's build GPT from scratch", "Let's build the GPT
Tokenizer", "Intro to Large Language Models" — none of it is here.

Consequence for this wiki: **any rule requiring corroboration across two
independent places must find its second source in the blog or the repos.** The
cross-source test is therefore weaker than it would be with lectures present,
and `rules.md` says so explicitly rather than implying otherwise.

Partial, non-substituted mitigation: companion code for several lectures does
exist in `raw/github/` (`nn-zero-to-hero`, `build-nanogpt`, `ng-video-lecture`,
`minbpe`). That is the code he wrote alongside the talks, **not** the spoken
transcripts that were requested, so it was not swapped in here.

## To fix

Add `youtube.com` (and `www.youtube.com`) to the environment's allowed domains,
keeping the default package-manager list, then re-run this source and rebuild its
manifest.
