# Source — blog

**Raw path:** `raw/blog/` · **Manifest:** `raw/blog/manifest.json`
**179 files · 110,657 words · 10 failures**

The densest source of his *written* thinking in this corpus, and the only one
where he writes long-form prose for a general reader.

## What it holds

| Folder | Contents |
| --- | --- |
| `karpathy.github.io/_posts/` | 23 posts, 2011-04-27 → 2026-02-12, raw Jekyll markdown with YAML front matter intact |
| `karpathy.github.io/nntutorial.md` | "Hacker's Guide to Neural Networks" — 82KB long-form, sits at repo root, *not* in `_posts/` |
| `karpathy.github.io/` | `about.md`, `index.html`, `feed.xml`, layouts, CSS, 134 image assets |
| `paper-notes/` | `matching_networks.md`, `vin.md`, `wikireading.md` + figures |

## The posts

```
2011-04-27  manually-classifying-cifar10          2015-11-20  ai
2012-10-22  state-of-computer-vision              2016-05-31  rl
2013-11-23  chrome-extension-programming          2016-09-07  phd
2013-11-27  quantifying-hacker-news               2018-01-20  medium  (stub)
2014-04-26  datascience-weekly-interview          2019-04-25  recipe
2014-07-01  switching-to-jekyll                   2020-06-11  biohacking-lite
2014-07-02  visualizing-top-tweeps-with-t-sne     2021-03-27  forward-pass
2014-07-03  feature-learning-escapades            2021-06-21  blockchain
2014-08-03  quantifying-productivity              2022-03-14  lecun1989
2014-09-02  competing-against-a-convnet-imagenet  2026-02-12  microgpt
2015-03-30  breaking-convnets
2015-05-21  rnn-effectiveness
2015-10-25  selfie
```

Highest-yield for this wiki: `2019-04-25-recipe` (his training methodology,
stated as explicit rules), `2016-09-07-phd` (research taste), `nntutorial.md`
(his teaching philosophy stated outright), `2015-05-21-rnn-effectiveness`, and
`2026-02-12-microgpt` (the only recent datapoint).

Four files yield no usable prose and are deliberately not quoted: `2015-11-20-ai`
and `2021-03-27-forward-pass` are short fiction, `2018-01-20-medium` is a
redirect stub, and `2014-04-26-datascience-weekly-interview` is a 12-line link
post.

**Note:** there is no Software 2.0 essay in this corpus. It was published on
Medium, which is blocked, so the theme is only visible here as indirect traces.

## How it was collected

Cloned from the `karpathy.github.io` GitHub repo, **not scraped**. The rendered
site is blocked by this environment's network policy, but the blog is a Jekyll
site, so the repo carries every post as raw markdown with front matter intact —
reachable *and* higher fidelity than scraped HTML would have been. `.git` was
stripped after cloning; nothing was reformatted.

## What is missing — read before drawing conclusions

**This source is badly skewed to the early years.** Only two captured posts are
dated after 2021.

- `karpathy.bearblog.dev`, where he has been writing more recently, is **blocked**
  by network policy. The entire bearblog era is absent.
- `_posts/2018-01-20-medium.markdown` is a **stub pointing at Medium**, which is
  also blocked. So the Medium gap is an acknowledged hole in the record, not a
  hypothetical one.
- Seven candidate writing repos (`karpathy/blog`, `notes`, `writing`, `essays`,
  `random`, `karpathy-blog`, `karpathy.bearblog.dev`) did not resolve.

Any conclusion drawn from this source describes **2011–2021 Karpathy**. Do not
present it as how he writes or thinks now.
