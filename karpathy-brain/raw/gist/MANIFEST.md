# Manifest — `gist`

Generated: 2026-10-06T18:15:08.934216+00:00

- Files: **1** (1 text, 0 binary)
- Total words: **1,959**
- Total bytes: **11,985**
- Failures: **1**

## Collection method

```json
{
  "source": "gist",
  "subject": "Andrej Karpathy (gist.github.com/karpathy)",
  "collected_at_utc": "2026-10-06",
  "method": "Cloned the gist over git (`git clone https://gist.github.com/442a6bf555914893e9891c11519de94f`). gist.github.com is reachable over the git protocol in this environment even though the GitHub web and API hosts are blocked.",
  "gist_url": "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f",
  "why_added": "Supplied directly by the user as the framework for the wiki. It is Karpathy's own public writing, so it is filed as a raw source in its own right rather than kept loose outside the corpus. Added, not edited — no existing raw file was touched.",
  "enumeration": "Single known gist. No listing of his other gists was possible: the GitHub API is blocked for this session, so there is no way to enumerate gists by user.",
  "completeness_caveat": "This is ONE gist, the one the user supplied. Karpathy has other public gists that are not collected here, and this crawl cannot enumerate them.",
  "blocked_hosts": [
    "api.github.com",
    "github.com (web)"
  ]
}
```

## Files

| File | Words | Bytes |
| --- | ---: | ---: |
| `llm-wiki.md` | 1,959 | 11,985 |

## Failures

| Target | Reason | Error |
| --- | --- | --- |
| `https://api.github.com/users/karpathy/gists` | blocked — cannot enumerate his other public gists | GitHub API is bound to the session repo; returns 403 for non-configured paths |
