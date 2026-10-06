---
name: karpathy-teach
description: Hand a task to the karpathy subagent and grade its answer against the seven rules before showing it. Use when you want something built or explained the Karpathy way — from scratch, minimal, incremental, verified against a reference, and actually run — and you want the output checked rather than trusted.
---

# karpathy-teach

Route the task to the `karpathy` subagent, then **grade the result before the
user sees it**. The grading is the point: the agent states the rules, this skill
checks they were actually followed.

## Step 1 — hand off

Launch the `karpathy` subagent with the user's task, verbatim, plus any context
it needs (relevant file paths, what "done" means, constraints already agreed).

Do not pre-solve the task. Do not rewrite the ask into your own plan. Hand over
the real request and let the agent work.

If the task is pure conversation with nothing to build, explain, verify or run,
say so and answer directly — do not spawn the agent for the sake of it.

## Step 2 — grade against the seven rules

Score the returned answer. For each rule: **pass**, **fail**, or **n/a** (with a
reason n/a is legitimate — "no code was written" makes rules 2–6 n/a, "nothing
was claimed about Karpathy" makes the citation check n/a).

| # | Rule | What a fail looks like |
| --- | --- | --- |
| 1 | Built from scratch | Pulled in a dependency that was avoidable, with no justification given |
| 2 | Small; line count stated | No line count reported, or the code sprawled without comment |
| 3 | Complexity paid its way | Added machinery with no stated benefit, or accepted a bad trade |
| 4 | One unverified thing at a time | Several unverified changes stacked, then run once at the end |
| 5 | Verified against a reference | No reference, no diff, no hand-checked case — "it looks right" |
| 6 | Ran it; measured; kept negatives | **`Ran:` is "nothing" while code was written.** Or results asserted, not shown. Or a negative result quietly dropped |
| 7 | Taught via code and intuition | Explanation is derivation-first or abstract, with no runnable example |

Then two structural checks:

- **Citations.** Every claim about Karpathy cites a `karpathy-brain/wiki/` page.
  An uncited claim about him is a fail — including a true one.
- **Ending block.** The answer ends with `Ran:` / `Output:` / `Changed:`, filled
  in honestly. A missing or hand-waved block is a fail.

## Step 3 — act on the grade

- **All pass (or legitimately n/a)** → show the answer, with the grade appended.
- **Any fail** → **send it back to the same agent once**, naming the specific
  failed rules and what is missing. Do not fix it yourself; the agent must meet
  its own standard. Then re-grade.
- **Still failing after one send-back** → show the user the answer *and* the
  failed rules, explicitly, rather than quietly passing it off. An honest fail is
  more useful than a laundered pass.

Rule 6 is the one that fails most often and matters most: an answer that wrote
code and ran nothing is not finished work, however good the code looks. This
project also enforces that at the harness level — `.claude/hooks/karpathy_run_gate.py`
blocks the turn from ending with
*Karpathy rule, run it before you say it works.*

## Step 4 — show the grade

Append this to whatever you show the user:

```
Karpathy grade
  1 from scratch        pass / fail / n/a
  2 small, lines stated  …
  3 complexity paid      …
  4 one thing at a time  …
  5 verified vs reference …
  6 ran it, measured     …
  7 taught via code      …
  citations              …
  ending block           …
  → <verdict, and what was sent back if anything>
```

Never hide a fail. The grade is the product.
