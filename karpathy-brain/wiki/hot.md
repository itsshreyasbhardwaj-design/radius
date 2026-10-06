# Hot — how Karpathy thinks

The one page. Read this first; drill into `rules.md`, `principles.md`,
`methods.md` only if you need evidence.

**The core move:** rebuild the thing from scratch until it is small enough to
understand, then check it against something already known to work.

## The seven rules

1. **Build it from scratch, with nothing underneath you.** — *"what I cannot create I do not understand", what better way to do this than implement it from scratch?*
2. **Keep it small enough to hold in your head; count the lines.** — *"Both are tiny, with about 100 and 50 lines of code respectively."*
3. **Make complexity pay its way, or reject it.** — *"I may reject the PR because the complexity is not worth it."*
4. **Add one unverified thing at a time.** — *"get that to work, and then generalize it later making sure that I get the same result."*
5. **Assume failure is silent; verify against a reference.** — *"your misconfigured neural net will throw exceptions only if you're lucky"*
6. **Run it and measure; keep the negative results.** — *"Classifying as negative result and reverting back to FineWeb-edu for now."*
7. **Teach through code and intuition, and make them build it.** — *"code and physical intuitions instead of mathematical derivations"*

Sources and corroboration for each: `rules.md`.

## What he is for

Understanding, measured by whether the essence survives being stripped down —
*"if you understand microgpt, you understand the algorithmic essence."* Simplicity
as a target, not a consolation — *"I cannot simplify this any further."* Smallest
tool first — *"One should always try a BB gun before reaching for the Bazooka."*

## What he is against

Abstraction you did not choose. PyTorch's LayerNorm is *"buried 30 layers deep in
the code, behind an inscrutable dynamical dispatcher"*; autocast is *"magic we
don't control"*; a framework with *"a 1000 knobs controlling inscrutible code"*.
Not because they are big — because they stand between you and the mechanism.

## How he picks what to work on

*"You're not just solving problems - that's merely the simple inner loop."* The
real work is *"figuring out what problems are worth solving and what problems are
ripe for solving."* And go bigger than feels safe: *"a 10x more important problem
is at most 2-3x harder to achieve."*

## What this corpus cannot tell you

Three gaps that bound every claim here:

- **No lectures.** YouTube was blocked, so his spoken teaching — most of his
  teaching output — is absent. Every rule is corroborated from blog + repos only.
- **No X posts.** Blocked, and no credential. His most frequent, most informal
  record is missing.
- **Blog skews pre-2021.** His bearblog-era writing is blocked, and Software 2.0
  lives on Medium, also blocked.

So: this is the Karpathy of long-form writing and published code. Confident about
how he builds; thinner on how he teaches live, and on what he thinks now.
