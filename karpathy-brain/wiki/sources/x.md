# Source — x

**Raw path:** `raw/x/` · **Manifest:** `raw/x/manifest.json`
**0 files · 0 words · 4 failures — THIS SOURCE IS EMPTY**

## What was intended

Read the TwitterAPI.io key from the `.env` file, then page through `@karpathy`'s
posts via the TwitterAPI.io user timeline endpoint, saving each page of raw JSON.

## What happened

Two independent blockers, either of which alone is fatal.

**1. No credential.** There is no `.env` file anywhere in this environment.
`find / -name .env` returns nothing, and no environment variable matching
twitter/twtr/x_api is set. The repository's `.gitignore` excludes `.env*`, so it
was never committed and did not travel with the fresh clone this cloud session
works from.

**2. No route.** `api.twitterapi.io`, `twitterapi.io` and `x.com` are all refused
at the proxy CONNECT layer with 403 Forbidden.

No key value was requested, printed, or stored anywhere in this corpus.

## Why this gap matters

X is where he posts most frequently and most informally — reactions, short
opinions, work-in-progress notes. It is the highest-frequency, most recent, and
most unguarded record of his thinking, and none of it is here.

Combined with the blog being skewed pre-2021 and the lectures being absent, the
corpus has **no good coverage of his recent, informal thinking at all**. Pages in
this wiki describe the Karpathy visible in long-form writing and published code,
which is a real but partial view.

## To fix

Both blockers must be cleared:

- Supply the TwitterAPI.io key to the environment as a **secret / environment
  variable** — not a committed file.
- Add `api.twitterapi.io` to the environment's allowed domains.

Then re-run this source and rebuild its manifest.
