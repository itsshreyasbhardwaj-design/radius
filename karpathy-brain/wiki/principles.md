# Principles — what he believes

What shows up repeatedly as belief rather than procedure. Procedure lives in
`methods.md`; the seven corroborated rules live in `rules.md`.

Every claim here carries a verbatim quote from `raw/`. Where a belief rests on a
single place, it is marked **[single-source]** and should be treated as an
observation, not a pattern.

---

## Understanding is the point; capability is the by-product

He frames not-understanding as a predictor of failure, not merely a discomfort.

> "If you insist on using the technology without understanding how it works you are likely to fail."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

And he treats the test of understanding as whether the essence survives being
stripped down:

> "All of these are important engineering and research contributions but if you understand microgpt, you understand the algorithmic essence."
> — `blog/karpathy.github.io/_posts/2026-02-12-microgpt.markdown`

> "Finally, I'd like to stress that I tried hard to keep the code itself clean, readable and hackable. You should not have feel scared to read the code and understand how it works."
> — `github/minbpe/README.md`

## Abstraction you did not choose is a liability

The recurring complaint is not that frameworks are big, but that they put
distance between you and the thing.

> "That's because it is buried 30 layers deep in the code, behind an inscrutable dynamical dispatcher, in some possibly auto-generated CUDA code"
> — `github/llm.c/doc/layernorm/layernorm.md`

> "autocast is "magic we don't control" — it silently decides which ops run in which precision via internal allowlists."
> — `github/nanochat/dev/LOG.md`

> "In particular, this repo is not a complex framework with a 1000 knobs controlling inscrutible code across a nested directory structure of hundreds of files."
> — `github/llama2.c/README.md`

> "E.g. some large functions have as much as 90% unused code behind various branching statements that is unused in the default setting of simple language modeling"
> — `github/minGPT/README.md`

His stated remedy is to make the hidden thing explicit and accept the cost:

> "By making precision explicit, we gain fine-grained control (e.g. can experiment with fp32 norms) and eliminate an unnecessary layer of abstraction."
> — `github/nanochat/dev/LOG.md`

## Simplicity is a target, not a consolation prize

> "I cannot simplify this any further."
> — `blog/karpathy.github.io/_posts/2026-02-12-microgpt.markdown`

> "Everything else is just efficiency."
> — `blog/karpathy.github.io/_posts/2026-02-12-microgpt.markdown`

> "One should always try a BB gun before reaching for the Bazooka."
> — `blog/karpathy.github.io/_posts/2016-05-31-rl.markdown`

> "The truth is that getting these models to work can be tricky, requires care and expertise, and in many cases could also be an overkill, where simpler methods could get you 90%+ of the way there."
> — `blog/karpathy.github.io/_posts/2016-05-31-rl.markdown`

## Pick the problem, not just the solution

His sharpest statements about research are about *problem selection* over
problem solving.

> "You're not just solving problems - that's merely the simple inner loop."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "You spend most of your time on the outer loop, figuring out what problems are worth solving and what problems are ripe for solving."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "This is a fallacy - in my experience a 10x more important problem is at most 2-3x harder to achieve."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "It's because thinking 10x forces you out of the box, to confront the real limitations of an approach, to think from first principles, to change the strategy completely, to innovate."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "Incremental work is a paper that enhances something existing by making it more complex and gets 2% extra on some benchmark."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "Think for yourself and from first principles."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "Do things others don't do but should."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

> "Step off the treadmill that has been put before you."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

Note the self-assessment underneath all of this — he describes taste as something
he lacked and acquired, not as innate:

> "In particular, I think I had a terrible taste coming in to the PhD."
> — `blog/karpathy.github.io/_posts/2016-09-07-phd.markdown`

**Caveat:** this section leans almost entirely on one post. It is included
because it is unusually explicit, but it is **weakly corroborated** by the
standard `rules.md` applies, and no rule was built from it.

## A change should generalise, not just win

> "But any candidate changes to the repo have to be principled enough that they work for all settings of depth."
> — `github/nanochat/README.md`

> "So your change must be principled enough that it can easily generalize to other model depths, so that we can sweep out a miniseries."
> — `github/nanochat/dev/LEADERBOARD.md`

## Magic-to-simplicity gaps are where he writes

A useful tell for predicting what he will work on next:

> "Whenever there is a disconnect between how magical something seems and how simple it is under the hood I get all antsy and really want to write a blog post."
> — `blog/karpathy.github.io/_posts/2016-05-31-rl.markdown`

## Software 2.0 — present only as a trace **[single-source]**

The idea appears, but the essay that defines it is **not in this corpus** — it
was published on Medium, which is blocked.

> "We just trained the LSTM on raw data and it decided that this is a useful quantitity to keep track of."
> — `blog/karpathy.github.io/_posts/2015-05-21-rnn-effectiveness.markdown`

> "Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like."
> — `github/llm-council/README.md`

Do not treat this section as a summary of his Software 2.0 position. It is the
residue of it that survives in the reachable sources.

---

**Coverage caveat.** No lectures and no X posts are in this corpus, and the blog
is skewed pre-2021. These are the beliefs visible in long-form writing and
published code. See `wiki/sources/youtube.md` and `wiki/sources/x.md`.
