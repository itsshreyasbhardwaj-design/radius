# karpathy-brain

Raw collection of Andrej Karpathy's public output. One subfolder per source under
`raw/`, each with a manifest listing every file with its word count and everything
that failed.

**Nothing here is summarized, cleaned, deduplicated or interpreted.** This is a
collection pass only. Read the caveats below before building anything on top of it.

## Status

| Source | Files | Words | Failures | State |
| --- | ---: | ---: | ---: | --- |
| `raw/blog` | 179 | 110,657 | 10 | collected |
| `raw/github` | 3,587 | 4,796,444 | 155 | collected |
| `raw/youtube` | 0 | 0 | 4 | **failed — host blocked** |
| `raw/x` | 0 | 0 | 4 | **failed — no credential, host blocked** |
| **Total** | **3,766** | **4,907,101** | **173** | 125 MB |

## Layout

```
karpathy-brain/
  README.md                          this file
  tools/
    build_manifest.py                shared manifest builder — one schema for every source
    annotate_github_provenance.py    measures fork/dataset share of the github source
  raw/<source>/
    manifest.json                    machine-readable: per file path, bytes, word
                                     count, sha256, binary flag; plus collection
                                     method and the full failure list
    MANIFEST.md                      the same, human-readable
    _crawl/
      meta.json                      how it was collected, and what it misses
      failures.json                  every target that failed, with the real error
      provenance.json                github only — authorship measurement
      *.stderr.txt                   youtube only — captured tool errors as evidence
```

Regenerate any manifest after changing a source:

```
python3 -I karpathy-brain/tools/build_manifest.py karpathy-brain/raw/<source> <source>
```

## Caveats that change how you should use this

**1. The github word count is not Karpathy's writing.** Being in his account is not
the same as being written by him. Measured in `raw/github/_crawl/provenance.json`:

- **66.3%** of words are forks of other people's projects — `transformers` is a fork
  of huggingface/transformers and alone is 64.8% of the source; `nn` is a fork of
  torch/nn.
- **18.4%** are vendored datasets, fixtures and lockfiles. The tinyshakespeare corpus
  appears three separate times, across `build-nanogpt`, `char-rnn` and
  `ng-video-lecture`.
- **~15.3%** is plausibly Karpathy-authored.

Nothing was deleted, because this layer is meant to be raw. Filter at the point of
use, not by trusting the headline number.

**2. The blog is skewed to the early years.** Only two captured posts are dated after
2021. `karpathy.bearblog.dev` is blocked by network policy, so the entire bearblog era
is absent, and `_posts/2018-01-20-medium.markdown` is a stub pointing at Medium, which
is also blocked. Treating this as his complete blog writing would badly misrepresent
how he writes now.

**3. No video transcripts and no X posts.** Both sources are empty. `yt-dlp` and
`youtube-transcript-api` installed fine, but every YouTube request was refused at the
proxy. For X there was no credential in the environment *and* the API host was blocked.

**4. The github repo list may be incomplete.** The GitHub user-listing API is
unavailable to this session, so repos were enumerated by verifying a 203-name
candidate list with `git ls-remote` rather than from an authoritative listing. Any
public repo whose name was not guessed is silently missing, and this crawl cannot
tell how many such repos exist.

**5. Corpus files are force-added to git.** The cloned repos carry their own
`.gitignore` files; with `.git` stripped these act as nested ignore rules and would
silently exclude real corpus directories, leaving the manifests describing files git
never stored.

## To fill the gaps

- Add `youtube.com`, `api.twitterapi.io` and `karpathy.bearblog.dev` to the
  environment's allowed domains, keeping the default package-manager list.
- Supply the TwitterAPI.io key as an environment secret. Do not commit it — the repo
  `.gitignore` excludes `.env*`, which is why it was not available here.

Then re-run those sources and rebuild their manifests.
