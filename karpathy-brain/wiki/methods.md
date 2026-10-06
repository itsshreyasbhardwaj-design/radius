# Methods — how he actually works and teaches

Procedure, as opposed to belief (`principles.md`) or the seven corroborated
rules (`rules.md`). Every claim carries a verbatim quote from `raw/`.

---

## How he starts a problem

**Look at the data before touching the model.**

> "The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

> "That is - you want to visualize *exactly* what goes into your network, decoding that raw tensor of data and labels into visualizations."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

**Start from something known to work, not from your own idea.**

> "I always advise people to simply find the most related paper and copy paste their simplest architecture that achieves good performance."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

## How he moves

**Slowly, with a hypothesis per step.**

> "If writing your neural net code was like training one, you'd want to use a very small learning rate and guess and then evaluate the full test set after every iteration."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

**The tightest possible loop: change → run → compare.**

> "I like to change something in the code, re-run a d12 (or a d16 etc) and see if it helped, in an iteration loop."
> — `github/nanochat/README.md`

**Specific first, general later — and prove the generalisation did not change
the answer.**

> "I like to write a very specific function to what I'm doing right now, get that to work, and then generalize it later making sure that I get the same result."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

## How he debugs

**Smallest possible reproduction.**

> "Overfit a single batch of only a few examples (e.g. as little as two)."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

**A trusted reference beside the new thing.**

> "To run the unit tests you will have to install [PyTorch](https://pytorch.org/), which the tests use as a reference for verifying the correctness of the calculated gradients."
> — `github/micrograd/README.md`

> "You'll see that this first forwards the reference code on the CPU, then it runs kernel 1 on the GPU, compares the results to check for correctness, and then runs a number of configurations of this kernel"
> — `github/llm.c/dev/cuda/README.md`

**Make the tooling let you step through it.**

> "debugging tip: when you run the `make` command to build the binary, modify it by replacing `-O3` with `-g` so you can step through the code in your favorite IDE (e.g. vscode)."
> — `github/llm.c/README.md`

**What he says the job actually requires.**

> "The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail."
> — `blog/karpathy.github.io/_posts/2019-04-25-recipe.markdown`

## How he reads other people's results

Sceptically, and arithmetically. His paper notes are the clearest example —
he checks the numbers rather than accepting them.

> "The original image is claimed to be so resized from original 28x28 to 1x1x64, which doesn't make sense because factor of 2 downsampling 4 times is reduction of 16, and 28/16 is a non-integer >1."
> — `blog/paper-notes/matching_networks.md`

> "I can't find the MANN numbers of 82.8% and 94.9% in their paper [21]; not clear where they come from."
> — `blog/paper-notes/matching_networks.md`

> "Unfortunately, I'm not sure why the authors preferred breadth of experiments and sacrificed depth of experiments."
> — `blog/paper-notes/vin.md`

He applies the same scepticism to his own reproductions:

> "I verified that just swapping tanh -> relu in the original network did not give substantial gains, so most of the improvement here is coming from the addition of dropout."
> — `blog/karpathy.github.io/_posts/2022-03-14-lecun1989.markdown`

> "I was not able to reproduce single-forward-pass gains that the paper alludes to when training with multiple masks, might be doing something wrong."
> — `github/pytorch-made/README.md`

And to his own measurements:

> "An additional way to see that BIA is making stuff up is that it shows me losing lean body mass over time."
> — `blog/karpathy.github.io/_posts/2020-06-11-biohacking-lite.markdown`

---

## How he teaches

**Code and physical metaphor, in place of derivation.**

> "My exposition will center around code and physical intuitions instead of mathematical derivations."
> — `blog/karpathy.github.io/nntutorial.md`

> "The derivative can be thought of as a force on each input as we pull on the output to become higher."
> — `blog/karpathy.github.io/nntutorial.md`

> "Think of each operation as a little lego block: it takes some inputs, produces an output (the forward pass), and it knows how its output would change with respect to each of its inputs (the local gradient)."
> — `blog/karpathy.github.io/_posts/2026-02-12-microgpt.markdown`

**Write the explanation you wish you had been given.**

> "Basically, I will strive to present the algorithms in a way that I wish I had come across when I was starting out."
> — `blog/karpathy.github.io/nntutorial.md`

**Leave the construction order visible.**

> "The git commits were specifically kept step by step and clean so that one can easily walk through the git commit history to see it built slowly."
> — `github/build-nanogpt/README.md`

> "Publishing here as a Github repo so people can easily hack it, walk through the `git log` history of it, etc."
> — `github/ng-video-lecture/README.md`

**Make the learner do the work, with the answer available but not first.**

> "I recommend you work through the exercise yourself but work with it in tandem and whenever you are stuck unpause the video and see me give away the answer."
> — `github/nn-zero-to-hero/README.md`

> "Build your own GPT-4 Tokenizer!"
> — `github/minbpe/exercise.md`

**Give a cheap, vivid first win.**

> "If you are not a deep learning professional and you just want to feel the magic and get your feet wet, the fastest way to get started is to train a character-level GPT on the works of Shakespeare."
> — `github/nanoGPT/README.md`

**Admit what the teaching left out.**

> "NOTE: sadly I did not go too much into model initialization in the video lecture, but it is quite important for good performance."
> — `github/ng-video-lecture/README.md`

> "This is an early code release that works great but is slightly hastily released and probably requires some code reading of inline comments (which I tried to be quite good with in general)."
> — `github/neuraltalk2/README.md`

---

**Coverage caveat.** The teaching section is built from written artifacts only —
tutorials, READMEs, exercise files. His lectures are absent from this corpus
(`wiki/sources/youtube.md`), so how he teaches *live* is not evidenced here.
