# Rules — how he builds and how he teaches

Seven rules, drawn from `raw/`. **A rule only appears here if it shows up in at
least two independent places** — two different posts, or a post and a repo.
Every quote below was verified character-for-character against the cited file by
`tools/verify_quotes.py` (160/160 verified, 0 rejected).

Tags: **[builds]** · **[teaches]**

---

## 1. Build it from scratch, with nothing underneath you — **[builds]**

He does not read the thing, he re-implements it, and he treats dependency-freedom
as the point rather than a constraint.

> "And in the spirit of "what I cannot create I do not understand", what better way to do this than implement it from scratch?"
> — `blog/karpathy.github.io/_posts/2021-06-21-blockchain.markdown:34`

> "I set out to re-implement t-SNE from scratch since doing so is the best way of learning something that I know of, and what better language to do this in than - Javascript! :)"
> — `blog/karpathy.github.io/_posts/2014-07-02-visualizing-top-tweeps-with-t-sne-in-Javascript.markdown:13`

> "LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython."
> — `github/llm.c/README.md:3`

> "Just me developing a pure Python from-scratch zero-dependency implementation of Bitcoin for educational purposes, including all of the under the hood crypto primitives such as SHA-256 and elliptic curves over finite fields math."
> — `github/cryptos/README.md:4`

**Corroboration:** 4 places, 2 sources, spanning 2014→2021. The t-SNE post and
the Bitcoin post state the same justification seven years apart.

---

## 2. Keep it small enough to hold in your head, and count the lines — **[builds]**

Line count is not incidental in his READMEs; he states it as a headline feature.

> "Both are tiny, with about 100 and 50 lines of code respectively."
> — `github/micrograd/README.md:6`

> "GPT is not a complicated model and this implementation is appropriately about 300 lines of code"
> — `github/minGPT/README.md:6`

> "the whole thing is 130 lines of Python only using numpy as a dependency"
> — `blog/karpathy.github.io/_posts/2016-05-31-rl.markdown:35`

> "It is only about 100 lines long and hopefully it gives a concise, concrete and useful summary of the above if you're better at reading code than text."
> — `blog/karpathy.github.io/_posts/2015-05-21-rnn-effectiveness.markdown:98`

**Corroboration:** 4 places, both sources. The habit is identical in blog prose
and in repo READMEs.

---

## 3. Make complexity pay its way — otherwise reject it — **[builds]**

Not "keep it simple" as taste, but an explicit exchange rate he applies to
specific changes, including his own.

> "If there is a PR that e.g. improves performance by 2% but it "costs" 500 lines of complex C code, and maybe an exotic 3rd party dependency, I may reject the PR because the complexity is not worth it."
> — `github/llm.c/README.md:199`

> "This repo still cares about efficiency, but not at the cost of simplicity, readability or portability."
> — `github/llama2.c/README.md:321`

> "Helped a tiny bit (~1e-4 of loss), abandoned to control complexity."
> — `github/nanochat/dev/LOG.md:608`

> "What we try to prevent very hard is the introduction of a lot of "unverified" complexity at once, which is bound to introduce bugs/misconfigurations that will take forever to find (if ever)."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown:44`

**Corroboration:** 4 places, both sources. The `nanochat` log is him applying the
rule against a change that *worked* — the gain was real and he dropped it anyway.

---

## 4. Add one unverified thing at a time — **[builds]**

Incremental by construction, with the increments left visible for others.

> "I like to write a very specific function to what I'm doing right now, get that to work, and then generalize it later making sure that I get the same result."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown:72`

> "I think this might be one helpful way to step through the code base, where you add one component at a time."
> — `blog/karpathy.github.io/_posts/2026-02-12-microgpt.markdown:478`

> "The git commits were specifically kept step by step and clean so that one can easily walk through the git commit history to see it built slowly."
> — `github/build-nanogpt/README.md:3`

**Corroboration:** 3 places, both sources, spanning 2019→2026 — the oldest and
newest writing in the corpus agree.

---

## 5. Assume failure is silent — verify against a reference — **[builds]**

The rule the Stop hook in this project enforces. His stated reason is that broken
things do not announce themselves.

> "Therefore, your misconfigured neural net will throw exceptions only if you're lucky; Most of the time it will train but silently work a bit worse."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown:38`

> "We are in pursuit of correctness and are very willing to give up time for staying sane."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown:62`

> "To run the unit tests you will have to install [PyTorch](https://pytorch.org/), which the tests use as a reference for verifying the correctness of the calculated gradients."
> — `github/micrograd/README.md:65`

> "You'll see that this first forwards the reference code on the CPU, then it runs kernel 1 on the GPU, compares the results to check for correctness, and then runs a number of configurations of this kernel"
> — `github/llm.c/dev/cuda/README.md:25`

**Corroboration:** 4 places, both sources. Note the pattern in the two repos is
the same mechanism — run a trusted implementation beside the new one and diff.

---

## 6. Run it and measure — keep the negative results — **[builds]**

He reports what happened, including when it was nothing, and when he could not
match the paper.

> "I prefer my answers based on data, not confirmation-bias-susceptible personal anecdotes"
> — `blog/karpathy.github.io/_posts/2014-08-03-quantifying-productivity.markdown:11`

> "I like to change something in the code, re-run a d12 (or a d16 etc) and see if it helped, in an iteration loop."
> — `github/nanochat/README.md:100`

> "Classifying as negative result and reverting back to FineWeb-edu for now."
> — `github/nanochat/dev/LOG.md:711`

> "This is close but not quite the same as what the paper reports."
> — `github/lecun1989-repro/README.md:29`

**Corroboration:** 4 places, both sources. `nanochat/dev/LOG.md` is a dated
experiment log that is mostly negative results — the strongest single piece of
evidence for this rule in the corpus.

---

## 7. Teach through code and physical intuition, not derivations — **[teaches]**

> "My exposition will center around code and physical intuitions instead of mathematical derivations."
> — `blog/karpathy.github.io/nntutorial.md:14`

> "My personal experience with Neural Networks is that everything became much clearer when I started ignoring full-page, dense derivations of backpropagation equations and just started writing code."
> — `blog/karpathy.github.io/nntutorial.md:14`

> "It is only about 100 lines long and hopefully it gives a concise, concrete and useful summary of the above if you're better at reading code than text."
> — `blog/karpathy.github.io/_posts/2015-05-21-rnn-effectiveness.markdown:98`

And the learner is made to build it, not watch it:

> "I recommend you work through the exercise yourself but work with it in tandem and whenever you are stuck unpause the video and see me give away the answer."
> — `github/nn-zero-to-hero/README.md:52`

> "Build your own GPT-4 Tokenizer!"
> — `github/minbpe/exercise.md:3`

**Corroboration:** 5 places, both sources.

---

## Honest limits on these seven

**The corroboration test is weaker than it looks, because one of the two obvious
sources is missing.** The brief suggested corroborating across "his blog and a
lecture". There are **no lectures in this corpus** — the YouTube source is empty
because the host is blocked (`wiki/sources/youtube.md`). Every rule above is
therefore corroborated across *blog + repos*, never blog + spoken teaching.

Consequences worth stating plainly:

- **Teaching is under-sampled.** Rule 7 rests on written artifacts — a tutorial,
  a README, an exercise file. His actual lecturing, which is most of his teaching
  output, is not represented at all. One rule out of seven is a floor set by the
  evidence, not a claim that he teaches less than he builds.
- **The rules skew toward building** for the same reason: code repos are the
  best-covered source.
- **Recency is thin.** Only two blog posts postdate 2021 and there are no X posts,
  so these are rules evidenced mainly from 2011–2021 plus recent repos.
- **Software 2.0 is absent.** It was published on Medium, which is blocked, so a
  well-known part of his thinking is not represented and no rule claims it.

A rule that nearly made it and was cut for overlap with #1: *never accept a black
box you could have opened* — supported by "If you insist on using the technology
without understanding how it works you are likely to fail."
(`blog/.../2019-04-25-recipe.markdown`), `llm.c`'s LayerNorm note about PyTorch
being "buried 30 layers deep in the code, behind an inscrutable dynamical
dispatcher", and `nanochat/dev/LOG.md` calling autocast "magic we don't control".
