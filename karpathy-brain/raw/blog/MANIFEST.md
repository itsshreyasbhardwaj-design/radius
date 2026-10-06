# Manifest — `blog`

Generated: 2026-10-06T17:04:22.074975+00:00

- Files: **179** (45 text, 134 binary)
- Total words: **110,657**
- Total bytes: **31,038,290**
- Failures: **10**

## Collection method

```json
{
  "source": "blog",
  "collected_at_utc": "2026-10-06T17:03:45Z",
  "method": "Cloned the Jekyll site source from GitHub (git clone --depth 1 --single-branch https://github.com/karpathy/karpathy.github.io) rather than scraping rendered HTML. Two reasons: (1) the rendered blog host karpathy.github.io is blocked by this environment's egress policy (403 CONNECT), so scraping was impossible; (2) even if reachable, the Jekyll repo is the raw truth — it contains the original post source as markdown in _posts/ with YAML front matter intact, plus about.md, index.html, feed.xml, _layouts/, _includes/, css/ and assets/, with no HTML template chrome, no navigation boilerplate and no lossy HTML-to-text conversion. The clone's .git directory was deleted after copying; no file was reformatted, converted or edited.",
  "targets_collected": [
    {
      "target": "https://github.com/karpathy/karpathy.github.io",
      "local_path": "karpathy.github.io/",
      "what": "Full Jekyll source of the karpathy.github.io blog: 23 posts in _posts/ as raw markdown, plus about.md, index.html, feed.xml, nntutorial.md (the 'Hacker's Guide to Neural Networks' long-form piece, which lives at the repo root rather than in _posts/), layouts, includes, css and image assets."
    },
    {
      "target": "https://github.com/karpathy/paper-notes",
      "local_path": "paper-notes/",
      "what": "Karpathy's long-form paper notes/reviews as raw markdown (matching_networks.md, vin.md, wikireading.md) plus figure images. Resolved via git ls-remote and cloned; .git stripped."
    }
  ],
  "posts_captured": 23,
  "date_range": {
    "earliest": "2011-04-27",
    "latest": "2026-02-12",
    "derived_from": "_posts/ filename date prefixes under karpathy.github.io/_posts/",
    "earliest_file": "2011-04-27-manually-classifying-cifar10.markdown",
    "latest_file": "2026-02-12-microgpt.markdown"
  },
  "additional_long_form_captured_outside_posts": [
    "karpathy.github.io/nntutorial.md",
    "paper-notes/matching_networks.md",
    "paper-notes/vin.md",
    "paper-notes/wikireading.md"
  ],
  "completeness_caveat": "THIS IS THE GITHUB-HOSTED BLOG ONLY AND IS NOT A COMPLETE PICTURE OF KARPATHY'S PUBLIC BLOG WRITING. Specifically: (1) all posts on his newer blog karpathy.bearblog.dev are MISSING — that host is blocked by this environment's egress policy (curl: (56) CONNECT tunnel failed, response 403), and no GitHub-hosted mirror of it was found; (2) any Medium posts are MISSING — medium.com/@karpathy is blocked the same way (curl: (56) CONNECT tunnel failed, response 403). Note that karpathy.github.io/_posts/2018-01-20-medium.markdown exists in this corpus as a pointer/stub referring readers to Medium, so the Medium gap is a real, acknowledged hole in the record rather than a hypothetical one. Treat the 2022-2026 period as especially under-covered: the GitHub blog has only two posts dated after 2021 (2022-03-14, 2026-02-12), while the bearblog era is entirely absent. Any downstream analysis must not treat this corpus as the full set of his blog writing.",
  "blocked_hosts": [
    "karpathy.github.io (rendered blog; 403 CONNECT — worked around by cloning the source repo)",
    "karpathy.bearblog.dev (403 CONNECT — content NOT recovered)",
    "medium.com (403 CONNECT — content NOT recovered)"
  ],
  "hosts_that_worked": [
    "github.com (git clone / git ls-remote over HTTPS)"
  ],
  "raw_fidelity_notes": [
    "Files are byte-identical to what git delivered; nothing was reformatted, converted, renamed or summarized.",
    "The .git directory was deleted from both clones.",
    "Each clone is --depth 1 --single-branch, so no revision history is present — only the current tip of the default branch.",
    "Binary image assets (png/jpeg/gif) were kept as-is and are reported as binary in the manifest."
  ]
}
```

## Files

| File | Words | Bytes |
| --- | ---: | ---: |
| `karpathy.github.io/.gitignore` | 2 | 16 |
| `karpathy.github.io/Readme.md` | 22 | 136 |
| `karpathy.github.io/_config.yml` | 38 | 342 |
| `karpathy.github.io/_includes/footer.html` | 141 | 3,533 |
| `karpathy.github.io/_includes/head.html` | 77 | 1,112 |
| `karpathy.github.io/_includes/header.html` | 94 | 1,509 |
| `karpathy.github.io/_layouts/default.html` | 27 | 245 |
| `karpathy.github.io/_layouts/page.html` | 143 | 1,384 |
| `karpathy.github.io/_layouts/post.html` | 153 | 1,475 |
| `karpathy.github.io/_posts/2011-04-27-manually-classifying-cifar10.markdown` | 782 | 4,873 |
| `karpathy.github.io/_posts/2012-10-22-state-of-computer-vision.markdown` | 1,182 | 6,590 |
| `karpathy.github.io/_posts/2013-11-23-chrome-extension-programming.markdown` | 1,715 | 11,196 |
| `karpathy.github.io/_posts/2013-11-27-quantifying-hacker-news.markdown` | 477 | 2,959 |
| `karpathy.github.io/_posts/2014-04-26-datascience-weekly-interview.markdown` | 77 | 673 |
| `karpathy.github.io/_posts/2014-07-01-switching-to-jekyll.markdown` | 713 | 4,562 |
| `karpathy.github.io/_posts/2014-07-02-visualizing-top-tweeps-with-t-sne-in-Javascript.markdown` | 1,625 | 11,062 |
| `karpathy.github.io/_posts/2014-07-03-feature-learning-escapades.markdown` | 2,680 | 17,769 |
| `karpathy.github.io/_posts/2014-08-03-quantifying-productivity.markdown` | 1,834 | 11,143 |
| `karpathy.github.io/_posts/2014-09-02-what-i-learned-from-competing-against-a-convnet-on-imagenet.markdown` | 3,140 | 20,174 |
| `karpathy.github.io/_posts/2015-03-30-breaking-convnets.markdown` | 3,670 | 23,250 |
| `karpathy.github.io/_posts/2015-05-21-rnn-effectiveness.markdown` | 8,014 | 53,579 |
| `karpathy.github.io/_posts/2015-10-25-selfie.markdown` | 4,264 | 27,876 |
| `karpathy.github.io/_posts/2015-11-20-ai.markdown` | 8,105 | 48,552 |
| `karpathy.github.io/_posts/2016-05-31-rl.markdown` | 7,153 | 44,741 |
| `karpathy.github.io/_posts/2016-09-07-phd.markdown` | 8,374 | 49,023 |
| `karpathy.github.io/_posts/2018-01-20-medium.markdown` | 122 | 738 |
| `karpathy.github.io/_posts/2019-04-25-recipe.markdown` | 3,903 | 23,695 |
| `karpathy.github.io/_posts/2020-06-11-biohacking-lite.markdown` | 5,395 | 34,227 |
| `karpathy.github.io/_posts/2021-03-27-forward-pass.markdown` | 1,304 | 7,682 |
| `karpathy.github.io/_posts/2021-06-21-blockchain.markdown` | 12,756 | 85,394 |
| `karpathy.github.io/_posts/2022-03-14-lecun1989.markdown` | 2,733 | 17,105 |
| `karpathy.github.io/_posts/2026-02-12-microgpt.markdown` | 5,676 | 37,111 |
| `karpathy.github.io/about.md` | 13 | 112 |
| `karpathy.github.io/assets/ai/.DS_Store` | — | 6,148 |
| `karpathy.github.io/assets/ai/digibrain.jpg` | — | 186,555 |
| `karpathy.github.io/assets/ai/eye2.jpg` | — | 40,211 |
| `karpathy.github.io/assets/ai/graph.png` | — | 281,739 |
| `karpathy.github.io/assets/ai/hand.jpg` | — | 179,527 |
| `karpathy.github.io/assets/ai/lifetree.gif` | — | 100,540 |
| `karpathy.github.io/assets/ai/neocortex.png` | — | 76,251 |
| `karpathy.github.io/assets/ai/ocean.jpeg` | — | 71,460 |
| `karpathy.github.io/assets/ai/psych.jpg` | — | 300,612 |
| `karpathy.github.io/assets/bio/atp_recycling.png` | — | 334,984 |
| `karpathy.github.io/assets/bio/atpspring.svg` | 2,288 | 87,151 |
| `karpathy.github.io/assets/bio/atpsynthesis.svg` | 1,297 | 61,967 |
| `karpathy.github.io/assets/bio/body_composition.png` | — | 114,609 |
| `karpathy.github.io/assets/bio/combustion.jpeg` | — | 86,213 |
| `karpathy.github.io/assets/bio/combustion2.png` | — | 137,089 |
| `karpathy.github.io/assets/bio/cookie.jpg` | — | 210,603 |
| `karpathy.github.io/assets/bio/dexa.png` | — | 78,966 |
| `karpathy.github.io/assets/bio/energy_metabolism_1.png` | — | 347,337 |
| `karpathy.github.io/assets/bio/expected_loss.png` | — | 35,163 |
| `karpathy.github.io/assets/bio/subway_map.png` | — | 292,255 |
| `karpathy.github.io/assets/bio/sweating.jpg` | — | 105,686 |
| `karpathy.github.io/assets/bio/weight.png` | — | 56,128 |
| `karpathy.github.io/assets/bio/weight_loss.gif` | — | 23,722 |
| `karpathy.github.io/assets/break/banana.jpeg` | — | 33,245 |
| `karpathy.github.io/assets/break/break1.jpeg` | — | 87,993 |
| `karpathy.github.io/assets/break/break2.jpeg` | — | 63,545 |
| `karpathy.github.io/assets/break/breakconv.png` | — | 107,219 |
| `karpathy.github.io/assets/break/fish.jpeg` | — | 85,286 |
| `karpathy.github.io/assets/break/fool1.jpeg` | — | 105,213 |
| `karpathy.github.io/assets/break/fool2.jpeg` | — | 104,407 |
| `karpathy.github.io/assets/break/noise1.jpeg` | — | 63,921 |
| `karpathy.github.io/assets/break/noise2.jpeg` | — | 64,649 |
| `karpathy.github.io/assets/break/rapeseed.jpeg` | — | 121,682 |
| `karpathy.github.io/assets/break/rapeseed2.jpeg` | — | 93,141 |
| `karpathy.github.io/assets/break/szegedy.jpeg` | — | 125,526 |
| `karpathy.github.io/assets/break/templates.jpeg` | — | 93,267 |
| `karpathy.github.io/assets/chrome1.jpeg` | — | 15,499 |
| `karpathy.github.io/assets/chrome2.jpeg` | — | 45,290 |
| `karpathy.github.io/assets/chrome3.jpeg` | — | 5,419 |
| `karpathy.github.io/assets/chrome4.jpeg` | — | 68,394 |
| `karpathy.github.io/assets/cifar_predict.jpg` | — | 152,974 |
| `karpathy.github.io/assets/cifar_preview.png` | — | 340,619 |
| `karpathy.github.io/assets/cifar_weirdimages.png` | — | 50,033 |
| `karpathy.github.io/assets/cnntsne.jpeg` | — | 155,930 |
| `karpathy.github.io/assets/hn.jpg` | — | 136,504 |
| `karpathy.github.io/assets/ilsvrc1.png` | — | 413,553 |
| `karpathy.github.io/assets/ilsvrc2.png` | — | 226,609 |
| `karpathy.github.io/assets/ilsvrc3.png` | — | 349,667 |
| `karpathy.github.io/assets/lecun/errors32.png` | — | 25,086 |
| `karpathy.github.io/assets/lecun/lecun1989.png` | — | 195,409 |
| `karpathy.github.io/assets/megoogle.jpg` | — | 18,792 |
| `karpathy.github.io/assets/microgpt.jpg` | — | 1,686,666 |
| `karpathy.github.io/assets/nips2012.jpeg` | — | 26,169 |
| `karpathy.github.io/assets/obamafunny.jpg` | — | 249,084 |
| `karpathy.github.io/assets/objectdiscovery.jpeg` | — | 39,455 |
| `karpathy.github.io/assets/phd/adviser.gif` | — | 71,140 |
| `karpathy.github.io/assets/phd/arxiv-papers.png` | — | 2,425,835 |
| `karpathy.github.io/assets/phd/code.jpg` | — | 142,273 |
| `karpathy.github.io/assets/phd/latex.png` | — | 114,802 |
| `karpathy.github.io/assets/phd/phds.jpg` | — | 415,165 |
| `karpathy.github.io/assets/phd/posters.jpg` | — | 722,881 |
| `karpathy.github.io/assets/phd/talk.jpg` | — | 89,092 |
| `karpathy.github.io/assets/rl/discounted.png` | — | 26,255 |
| `karpathy.github.io/assets/rl/episodes.png` | — | 45,069 |
| `karpathy.github.io/assets/rl/frostbite.jpg` | — | 31,040 |
| `karpathy.github.io/assets/rl/mdp.png` | — | 34,603 |
| `karpathy.github.io/assets/rl/montezuma.png` | — | 2,289 |
| `karpathy.github.io/assets/rl/nondiff1.png` | — | 48,695 |
| `karpathy.github.io/assets/rl/nondiff2.png` | — | 76,786 |
| `karpathy.github.io/assets/rl/pg.png` | — | 167,224 |
| `karpathy.github.io/assets/rl/policy.png` | — | 54,059 |
| `karpathy.github.io/assets/rl/pong.gif` | — | 16,291 |
| `karpathy.github.io/assets/rl/preview.jpeg` | — | 54,860 |
| `karpathy.github.io/assets/rl/rl.png` | — | 79,987 |
| `karpathy.github.io/assets/rl/sl.png` | — | 76,459 |
| `karpathy.github.io/assets/rl/weights.png` | — | 207,318 |
| `karpathy.github.io/assets/rnn/charseq.jpeg` | — | 84,774 |
| `karpathy.github.io/assets/rnn/diags.jpeg` | — | 68,679 |
| `karpathy.github.io/assets/rnn/diags_old.jpeg` | — | 86,311 |
| `karpathy.github.io/assets/rnn/house_generate.gif` | — | 626,173 |
| `karpathy.github.io/assets/rnn/house_read.gif` | — | 839,099 |
| `karpathy.github.io/assets/rnn/latex1.jpeg` | — | 161,316 |
| `karpathy.github.io/assets/rnn/latex2.jpeg` | — | 46,243 |
| `karpathy.github.io/assets/rnn/latex3.jpeg` | — | 231,685 |
| `karpathy.github.io/assets/rnn/latex4.jpeg` | — | 313,757 |
| `karpathy.github.io/assets/rnn/pane1.png` | — | 633,413 |
| `karpathy.github.io/assets/rnn/pane2.png` | — | 384,662 |
| `karpathy.github.io/assets/rnn/under1.jpeg` | — | 515,889 |
| `karpathy.github.io/assets/rnn/under2.jpeg` | — | 530,360 |
| `karpathy.github.io/assets/rnn/under3.jpeg` | — | 261,944 |
| `karpathy.github.io/assets/rnn/under4.jpeg` | — | 114,932 |
| `karpathy.github.io/assets/rssicon.svg` | 261 | 6,300 |
| `karpathy.github.io/assets/selfie/celebs_grid_render.jpg` | — | 1,944,422 |
| `karpathy.github.io/assets/selfie/cnnvis.jpg` | — | 117,496 |
| `karpathy.github.io/assets/selfie/crop2.jpg` | — | 70,897 |
| `karpathy.github.io/assets/selfie/crops1.jpg` | — | 128,002 |
| `karpathy.github.io/assets/selfie/gif2.gif` | — | 2,122,948 |
| `karpathy.github.io/assets/selfie/grid_render_all.jpg` | — | 867,353 |
| `karpathy.github.io/assets/selfie/grid_render_best.jpg` | — | 332,905 |
| `karpathy.github.io/assets/selfie/grid_render_continuum.jpg` | — | 903,642 |
| `karpathy.github.io/assets/selfie/grid_render_posneg.jpg` | — | 242,144 |
| `karpathy.github.io/assets/selfie/grid_render_tsne_reduced.jpg` | — | 346,544 |
| `karpathy.github.io/assets/selfie/grid_render_worst.jpg` | — | 202,042 |
| `karpathy.github.io/assets/selfie/males.jpg` | — | 183,840 |
| `karpathy.github.io/assets/selfie/selfiebot2.png` | — | 122,985 |
| `karpathy.github.io/assets/selfie/teaser.jpeg` | — | 399,109 |
| `karpathy.github.io/assets/selfie/useful.jpg` | — | 274,786 |
| `karpathy.github.io/assets/sportspredict.jpeg` | — | 156,994 |
| `karpathy.github.io/assets/tsne_eg.jpeg` | — | 52,376 |
| `karpathy.github.io/assets/tsne_preview.jpeg` | — | 93,579 |
| `karpathy.github.io/assets/tsne_sentprepro.jpeg` | — | 165,449 |
| `karpathy.github.io/assets/ulogme_mv1.jpeg` | — | 214,673 |
| `karpathy.github.io/assets/ulogme_mv2.jpeg` | — | 88,972 |
| `karpathy.github.io/assets/ulogme_mv3.jpeg` | — | 136,787 |
| `karpathy.github.io/assets/ulogme_sv1.jpeg` | — | 31,973 |
| `karpathy.github.io/assets/ulogme_sv2.jpeg` | — | 62,918 |
| `karpathy.github.io/assets/ulogme_sv3.jpeg` | — | 87,522 |
| `karpathy.github.io/assets/ulogme_sv4.jpeg` | — | 38,871 |
| `karpathy.github.io/assets/ulogmeoverview.jpeg` | — | 151,121 |
| `karpathy.github.io/assets/zeilercnnfeatures.jpeg` | — | 106,362 |
| `karpathy.github.io/css/main.css` | 1,360 | 10,218 |
| `karpathy.github.io/feed.xml` | 129 | 1,292 |
| `karpathy.github.io/index.html` | 44 | 369 |
| `karpathy.github.io/nntutorial.md` | 14,021 | 82,472 |
| `paper-notes/.gitignore` | 1 | 11 |
| `paper-notes/Readme.md` | 12 | 65 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-07 at 10.08.44 PM.png` | — | 305,266 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-07 at 11.14.26 PM.png` | — | 21,024 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-07 at 11.20.29 PM.png` | — | 37,851 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-07 at 11.57.10 PM.png` | — | 181,349 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-08 at 10.21.45 AM.png` | — | 231,111 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-08 at 10.27.46 AM.png` | — | 181,685 |
| `paper-notes/img/matching_networks/Screen Shot 2016-08-08 at 12.11.15 AM.png` | — | 71,608 |
| `paper-notes/img/vin/Screen Shot 2016-08-13 at 3.26.04 PM.png` | — | 23,355 |
| `paper-notes/img/vin/Screen Shot 2016-08-13 at 4.43.04 PM.png` | — | 55,113 |
| `paper-notes/img/vin/Screen Shot 2016-08-13 at 4.58.42 PM.png` | — | 178,341 |
| `paper-notes/img/vin/Screen Shot 2016-08-13 at 5.47.23 PM.png` | — | 81,847 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 1.53.11 PM.png` | — | 226,079 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 2.37.48 PM.png` | — | 34,765 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 2.38.24 PM.png` | — | 42,272 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 3.18.05 PM.png` | — | 60,893 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 4.07.18 PM.png` | — | 428,245 |
| `paper-notes/img/wikireading/Screen Shot 2016-08-07 at 4.22.13 PM.png` | — | 178,891 |
| `paper-notes/matching_networks.md` | 1,760 | 11,081 |
| `paper-notes/vin.md` | 1,530 | 9,642 |
| `paper-notes/wikireading.md` | 1,550 | 10,073 |

## Failures

| Target | Reason | Error |
| --- | --- | --- |
| `https://karpathy.github.io/` | blocked by environment egress policy | 403 CONNECT (proxy refused to open tunnel) — pre-verified as blocked before this crawl; not retried. Content recovered instead by cloning the Jekyll source repo github.com/karpathy/karpathy.github.io. |
| `https://karpathy.bearblog.dev/` | blocked by environment egress policy | curl: (56) CONNECT tunnel failed, response 403 (http_code 000) |
| `https://medium.com/@karpathy` | blocked by environment egress policy | curl: (56) CONNECT tunnel failed, response 403 (http_code 000) |
| `https://github.com/karpathy/blog` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/notes` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/writing` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/essays` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/random` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/karpathy-blog` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt) |
| `https://github.com/karpathy/karpathy.bearblog.dev` | repository does not exist / not accessible | git ls-remote: fatal: could not read Username for 'https://github.com': terminal prompts disabled (anonymous 404 → auth prompt). No GitHub-hosted mirror of the bearblog.dev posts was found. |
