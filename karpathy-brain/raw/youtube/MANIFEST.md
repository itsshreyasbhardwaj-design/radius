# Manifest — `youtube`

Generated: 2026-10-06T17:04:26.028163+00:00

- Files: **0** (0 text, 0 binary)
- Total words: **0**
- Total bytes: **0**
- Failures: **4**

## Collection method

```json
{
  "status": "FAILED — zero files collected",
  "collected_at_utc": "2026-10-06",
  "intended_method": "Enumerate the @AndrejKarpathy channel with yt-dlp, then pull caption transcripts for every lecture using youtube-transcript-api with yt-dlp as the fallback for auto-generated captions.",
  "tools_installed": {
    "yt-dlp": "2026.08.19",
    "youtube-transcript-api": "installed from PyPI (reachable)"
  },
  "what_actually_happened": "Both tools installed cleanly — PyPI is reachable. Every request to YouTube was refused at the proxy CONNECT layer with 403 Forbidden, so neither channel enumeration nor a single caption fetch succeeded. This is an environment network-policy denial, not a tool, version, or rate-limit problem.",
  "blocked_hosts": [
    "www.youtube.com",
    "youtube.com",
    "m.youtube.com"
  ],
  "root_cause": "The session's egress policy does not allow youtube.com. Nothing in this folder can be collected until that host is allowed.",
  "remedy": "Add youtube.com (and www.youtube.com) to Allowed domains in the cloud environment's Network access settings, keeping the default package-manager list, then re-run this source.",
  "completeness_caveat": "This source is EMPTY. No transcript of any Karpathy lecture was collected. Do not treat the corpus as covering his video lectures.",
  "partial_mitigation_available_but_not_applied": "Some lecture material exists as source in his GitHub repos (for example nn-zero-to-hero notebooks, build-nanogpt, ng-video-lecture) and is captured under raw/github/. That is companion code, NOT the spoken caption transcripts that were requested, so it was not substituted in here."
}
```

## Files

| File | Words | Bytes |
| --- | ---: | ---: |

## Failures

| Target | Reason | Error |
| --- | --- | --- |
| `https://www.youtube.com/@AndrejKarpathy/videos` | blocked by environment egress policy — yt-dlp could not enumerate the channel | ERROR: [youtube:tab] @AndrejKarpathy/videos: Unable to download API page: ('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden')). yt-dlp 2026.08.19. Full stderr in _crawl/ytdlp_channel.stderr.txt |
| `https://www.youtube.com/watch?v=kCc8FmEb1nY (yt-dlp --write-sub --write-auto-sub)` | blocked by environment egress policy — yt-dlp could not fetch captions for a representative lecture | ERROR: [youtube] kCc8FmEb1nY: Unable to download API page: ('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden')). Full stderr in _crawl/ytdlp_subtitles.stderr.txt |
| `youtube_transcript_api.YouTubeTranscriptApi().fetch('kCc8FmEb1nY')` | blocked by environment egress policy — youtube-transcript-api could not reach youtube.com | ProxyError: HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /watch?v=kCc8FmEb1nY (Caused by ProxyError('Unable to connect to proxy', OSError('Tunnel connection failed: 403 Forbidden'))) |
| `www.youtube.com / youtube.com / m.youtube.com` | blocked by environment egress policy at the CONNECT layer | curl: (56) CONNECT tunnel failed, response 403 — all three hostnames |
