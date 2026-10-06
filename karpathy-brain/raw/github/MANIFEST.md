# Manifest — `github`

Generated: 2026-10-06T17:08:22.814644+00:00

- Files: **3587** (3305 text, 282 binary)
- Total words: **4,796,444**
- Total bytes: **86,908,054**
- Failures: **155**

## Collection method

```json
{
  "source": "github",
  "subject": "Andrej Karpathy (github.com/karpathy)",
  "collected_at_utc": "2026-10-06T17:05:57Z",
  "method": "For each verified repo: `git clone --depth 1 --single-branch https://github.com/karpathy/<repo> <dest>`, then the `.git` directory was deleted from each checkout to save disk. Files are kept exactly as they came down, unmodified. No summarization or interpretation was performed.",
  "enumeration": "The GitHub user-listing API (https://api.github.com/users/karpathy/repos) is BLOCKED in this environment (the session is bound to one configured repo), and the `gh` CLI fails the same way. The plain web page https://github.com/karpathy, codeload.github.com, and third-party GitHub mirrors (ungh.cc, r.jina.ai, codetabs) are also blocked by egress policy (403 CONNECT). There was therefore no way to obtain an authoritative listing of the user's repositories. Instead, a curated candidate list of 203 plausible repo names was assembled from model knowledge (well-known projects, older/obscure projects, likely forks, and name variants), and every candidate was verified with `git ls-remote --heads https://github.com/karpathy/<name>`. Candidates that resolved were cloned. GitHub answers ls-remote for a nonexistent or non-public repo with an authentication challenge, which git reports as 'Authentication failed'; this was confirmed against a deliberately nonexistent control name, and borderline candidates were re-tested sequentially to rule out rate limiting.",
  "completeness_caveat": "THIS LIST MAY BE INCOMPLETE. No authoritative API listing of karpathy's repositories was available, so coverage is limited to repo names that were guessed and then verified. Any public repository whose name was not in the candidate list is silently missing from this collection, and there is no way to tell from this crawl how many such repositories exist. Renamed repositories may also have been missed. Treat the repo set as a high-confidence subset, not an exhaustive inventory.",
  "candidates_tested": 203,
  "candidates_resolved": 46,
  "repos_cloned": 45,
  "repos_cloned_list": [
    "EigenLibSVM",
    "Random-Forest-Matlab",
    "arxiv-sanity-lite",
    "arxiv-sanity-preserver",
    "build-nanogpt",
    "char-rnn",
    "convnetjs",
    "covid-sanity",
    "cryptos",
    "deep-vector-quantization",
    "find-birds",
    "forestjs",
    "gitstats",
    "karpathy",
    "lecun1989-repro",
    "llama2.c",
    "llm-council",
    "llm.c",
    "llm101n",
    "makemore",
    "micrograd",
    "minGPT",
    "minbpe",
    "nanoGPT",
    "nanochat",
    "neuraltalk",
    "neuraltalk2",
    "ng-video-lecture",
    "nipspreview",
    "nn",
    "nn-zero-to-hero",
    "paper-notes",
    "pytorch-made",
    "pytorch-normalizing-flows",
    "randomfun",
    "recurrentjs",
    "reinforcejs",
    "researchlei",
    "researchpooler",
    "scholaroctopus",
    "svmjs",
    "tf-agent",
    "transformers",
    "tsnejs",
    "ulogme"
  ],
  "candidates_not_resolved": [
    "Arxiv-Sanity",
    "Deep-Q-Learning",
    "MatlabScripts",
    "MatlabWrappers",
    "Random-Forest",
    "agents",
    "alexnet",
    "arxiv-bot",
    "arxiv-sanity",
    "atari",
    "autograd",
    "awesome",
    "bigram",
    "bio",
    "blog",
    "caffe",
    "calorie-ninja",
    "cifar10",
    "convnet-js",
    "cs231n",
    "cs231n.github.io",
    "cursor-tutor",
    "cvpr",
    "deep-learning-papers",
    "deep-learning-school",
    "deepdream",
    "deepspeech",
    "diffusion",
    "digit",
    "dinosaur",
    "dotfiles",
    "dqn",
    "dqn-tensorflow",
    "emoji",
    "eureka",
    "experiments",
    "forest-js",
    "fun",
    "gan",
    "googlenet",
    "gpt",
    "gpt-2",
    "grad-cam",
    "gradcheck",
    "gridworld",
    "gym",
    "hbase",
    "iccv",
    "icml",
    "image-captioning",
    "imagenet",
    "ipython-notebooks",
    "llama",
    "llama.cpp",
    "llamafile",
    "llm-viz",
    "llm.c-cuda",
    "llmc",
    "llms",
    "lstm",
    "lstm-char-cnn",
    "magicarp",
    "makemore-rs",
    "mathquiz",
    "matlab",
    "micrograd-cpp",
    "micrograd-rs",
    "mingpt-demo",
    "mini-llm",
    "minsearch",
    "ml-notes",
    "mnist",
    "modded-nanogpt",
    "mywiki",
    "nano-llama31",
    "nanoGPT-lecture",
    "nanoGPT-llama",
    "nanoGPT-mup",
    "nanoGPT2",
    "nanoRL",
    "nanoVLM",
    "nanoagent",
    "nanodiffusion",
    "nanoeval",
    "nanoflow",
    "nanogpt-mlx",
    "nanogpt-speedrun",
    "nanogpt.c",
    "nanogrpo",
    "nanot5",
    "neural-networks",
    "neural-style",
    "neural-vqa",
    "neuraltalk2.torch",
    "neuraltalk3",
    "nips",
    "notebooks",
    "notpron",
    "numpy-tutorial",
    "openai-gym",
    "pixelcnn",
    "playground",
    "policy-gradient",
    "pong",
    "puckworld",
    "pytorch",
    "pytorch-cnn",
    "pytorch-examples",
    "pytorch-gan",
    "pytorch-lightning",
    "pytorch-quantization",
    "pytorch-rl",
    "pytorch-transformer",
    "pytorch-tutorial",
    "pytorch-vae",
    "pytorch-vq-vae",
    "recurrent-js",
    "reinforce",
    "reinforce-js",
    "resnet",
    "rl",
    "rlgames",
    "rnn",
    "sanity",
    "scripts",
    "sketch-rnn",
    "sortfix",
    "sortfix-demo",
    "sortfixdemo",
    "starter-code",
    "svm-js",
    "talks",
    "tensorflow",
    "tiny-shakespeare",
    "tinyshakespeare",
    "torch",
    "torch-rnn",
    "torch7",
    "tsne",
    "tsne-js",
    "tsne-pytorch",
    "tsne-viz",
    "ttmik",
    "tweetnlp",
    "twitter-bot",
    "twitter-sentiment",
    "vae",
    "vgg",
    "vision",
    "vq-vae",
    "waterworld",
    "wavenet",
    "whisper",
    "word2vec",
    "zero-to-hero"
  ],
  "case_variant_duplicates_ignored": {
    "mingpt": "minGPT",
    "nanogpt": "nanoGPT"
  },
  "delegated": {
    "karpathy.github.io": "Verified to exist via git ls-remote, but NOT cloned here: it is the blog source and is delegated to the separate blog source agent."
  },
  "size_cap_policy": "Per-repo cap of ~500MB measured with `du -sm` after clone and .git removal; over-cap checkouts would be deleted and recorded in failures.json. No repo exceeded the cap. Whole-folder budget was ~6GB.",
  "total_files": 3587,
  "total_bytes": 86908054,
  "total_mb": 82.9,
  "blocked_hosts": [
    "api.github.com",
    "github.com (plain web pages / HTML listing, e.g. https://github.com/karpathy)",
    "codeload.github.com",
    "ungh.cc",
    "r.jina.ai",
    "codetabs.com"
  ],
  "working_hosts": [
    "github.com (git over HTTPS: git clone / git ls-remote)",
    "raw.githubusercontent.com"
  ],
  "provenance_warning": {
    "summary": "66.3% of this source's words come from two forks of other people's projects (transformers, nn), and a further 18.4% are vendored datasets and lockfiles. Only about 15.3% is plausibly Karpathy-authored. Do not weight by raw word count.",
    "detail_file": "_crawl/provenance.json"
  }
}
```

## Files

| File | Words | Bytes |
| --- | ---: | ---: |
| `EigenLibSVM/CMakeLists.txt` | 15 | 241 |
| `EigenLibSVM/Readme.md` | 177 | 1,158 |
| `EigenLibSVM/include/eigenlibsvm/eigen_extensions.h` | 521 | 4,796 |
| `EigenLibSVM/include/eigenlibsvm/svm_utils.h` | 222 | 1,817 |
| `EigenLibSVM/src/svm_utils.cpp` | 586 | 5,257 |
| `EigenLibSVM/test/svm_test.cpp` | 182 | 1,723 |
| `Random-Forest-Matlab/README.txt` | 231 | 1,887 |
| `Random-Forest-Matlab/data/lenna.jpg` | — | 20,401 |
| `Random-Forest-Matlab/demos/forestdemo.m` | 385 | 3,144 |
| `Random-Forest-Matlab/demos/svmdemo.m` | 218 | 1,823 |
| `Random-Forest-Matlab/lib/forestTest.m` | 85 | 649 |
| `Random-Forest-Matlab/lib/forestTrain.m` | 248 | 1,780 |
| `Random-Forest-Matlab/lib/localContrastNormalize.m` | 240 | 1,591 |
| `Random-Forest-Matlab/lib/mgd.m` | 359 | 2,414 |
| `Random-Forest-Matlab/lib/storage.m` | 18 | 111 |
| `Random-Forest-Matlab/lib/svmTest.m` | 69 | 687 |
| `Random-Forest-Matlab/lib/svmTrain.m` | 431 | 3,331 |
| `Random-Forest-Matlab/lib/treeTest.m` | 240 | 1,568 |
| `Random-Forest-Matlab/lib/treeTrain.m` | 255 | 1,627 |
| `Random-Forest-Matlab/lib/weakTest.m` | 148 | 1,087 |
| `Random-Forest-Matlab/lib/weakTrain.m` | 675 | 5,637 |
| `arxiv-sanity-lite/.gitignore` | 6 | 69 |
| `arxiv-sanity-lite/LICENSE` | 168 | 1,063 |
| `arxiv-sanity-lite/Makefile` | 37 | 213 |
| `arxiv-sanity-lite/README.md` | 357 | 2,284 |
| `arxiv-sanity-lite/arxiv_daemon.py` | 483 | 4,125 |
| `arxiv-sanity-lite/aslite/arxiv.py` | 292 | 2,643 |
| `arxiv-sanity-lite/aslite/db.py` | 517 | 4,883 |
| `arxiv-sanity-lite/compute.py` | 203 | 2,444 |
| `arxiv-sanity-lite/data/readme.md` | 30 | 194 |
| `arxiv-sanity-lite/requirements.txt` | 5 | 83 |
| `arxiv-sanity-lite/screenshot.jpg` | — | 497,891 |
| `arxiv-sanity-lite/send_emails.py` | 1,181 | 9,890 |
| `arxiv-sanity-lite/serve.py` | 2,107 | 16,749 |
| `arxiv-sanity-lite/static/favicon.png` | — | 6,408 |
| `arxiv-sanity-lite/static/paper_detail.js` | 36 | 490 |
| `arxiv-sanity-lite/static/paper_list.js` | 361 | 3,544 |
| `arxiv-sanity-lite/static/search.png` | — | 1,422 |
| `arxiv-sanity-lite/static/style.css` | 635 | 5,308 |
| `arxiv-sanity-lite/static/word_list.js` | 79 | 818 |
| `arxiv-sanity-lite/templates/about.html` | 159 | 1,148 |
| `arxiv-sanity-lite/templates/base.html` | 120 | 1,243 |
| `arxiv-sanity-lite/templates/index.html` | 473 | 4,480 |
| `arxiv-sanity-lite/templates/inspect.html` | 69 | 503 |
| `arxiv-sanity-lite/templates/profile.html` | 226 | 2,273 |
| `arxiv-sanity-lite/templates/stats.html` | 147 | 966 |
| `arxiv-sanity-lite/thumb_daemon.py` | 483 | 3,856 |
| `arxiv-sanity-preserver/.gitignore` | 12 | 94 |
| `arxiv-sanity-preserver/LICENSE.md` | 171 | 1,080 |
| `arxiv-sanity-preserver/README.md` | 1,040 | 6,958 |
| `arxiv-sanity-preserver/analyze.py` | 433 | 3,440 |
| `arxiv-sanity-preserver/buildsvm.py` | 269 | 2,210 |
| `arxiv-sanity-preserver/download_pdfs.py` | 161 | 1,242 |
| `arxiv-sanity-preserver/fetch_papers.py` | 523 | 4,592 |
| `arxiv-sanity-preserver/make_cache.py` | 425 | 3,572 |
| `arxiv-sanity-preserver/parse_pdf_to_text.py` | 222 | 1,612 |
| `arxiv-sanity-preserver/requirements.txt` | 37 | 248 |
| `arxiv-sanity-preserver/schema.sql` | 50 | 346 |
| `arxiv-sanity-preserver/serve.py` | 2,988 | 26,485 |
| `arxiv-sanity-preserver/static/as-common.js` | 1,119 | 10,329 |
| `arxiv-sanity-preserver/static/d3.min.js` | 2,806 | 146,658 |
| `arxiv-sanity-preserver/static/favicon.png` | — | 4,668 |
| `arxiv-sanity-preserver/static/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `arxiv-sanity-preserver/static/linkto.png` | — | 1,956 |
| `arxiv-sanity-preserver/static/marked.min.js` | 267 | 19,513 |
| `arxiv-sanity-preserver/static/missing.jpg` | — | 8,492 |
| `arxiv-sanity-preserver/static/save.png` | — | 1,029 |
| `arxiv-sanity-preserver/static/saved.png` | — | 652 |
| `arxiv-sanity-preserver/static/search.png` | — | 1,422 |
| `arxiv-sanity-preserver/static/style.css` | 1,000 | 8,023 |
| `arxiv-sanity-preserver/templates/account.html` | 749 | 7,291 |
| `arxiv-sanity-preserver/templates/discuss.html` | 1,112 | 11,658 |
| `arxiv-sanity-preserver/templates/main.html` | 1,047 | 10,700 |
| `arxiv-sanity-preserver/thumb_pdf.py` | 520 | 3,808 |
| `arxiv-sanity-preserver/twitter_daemon.py` | 841 | 7,452 |
| `arxiv-sanity-preserver/ui.jpeg` | — | 259,138 |
| `arxiv-sanity-preserver/utils.py` | 313 | 2,835 |
| `build-nanogpt/README.md` | 686 | 4,488 |
| `build-nanogpt/fineweb.py` | 377 | 3,512 |
| `build-nanogpt/hellaswag.py` | 858 | 7,713 |
| `build-nanogpt/input.txt` | 202,651 | 1,115,394 |
| `build-nanogpt/play.ipynb` | 1,150 | 11,211 |
| `build-nanogpt/train_gpt2.py` | 2,568 | 23,576 |
| `char-rnn/.gitignore` | 1 | 5 |
| `char-rnn/Readme.md` | 1,966 | 12,795 |
| `char-rnn/convert_gpu_cpu_checkpoint.lua` | 312 | 2,176 |
| `char-rnn/data/tinyshakespeare/input.txt` | 202,651 | 1,115,394 |
| `char-rnn/inspect_checkpoint.lua` | 117 | 954 |
| `char-rnn/model/GRU.lua` | 237 | 2,058 |
| `char-rnn/model/LSTM.lua` | 236 | 2,069 |
| `char-rnn/model/RNN.lua` | 143 | 1,135 |
| `char-rnn/sample.lua` | 773 | 6,035 |
| `char-rnn/train.lua` | 1,964 | 16,044 |
| `char-rnn/util/CharSplitLMMinibatchLoader.lua` | 874 | 7,455 |
| `char-rnn/util/OneHot.lua` | 70 | 670 |
| `char-rnn/util/misc.lua` | 50 | 344 |
| `char-rnn/util/model_utils.lua` | 462 | 5,151 |
| `convnetjs/LICENSE` | 170 | 1,077 |
| `convnetjs/Readme.md` | 749 | 5,961 |
| `convnetjs/bower.json` | 56 | 614 |
| `convnetjs/build/deepqlearn.js` | 1,541 | 13,702 |
| `convnetjs/build/util.js` | 251 | 1,722 |
| `convnetjs/build/vis.js` | 681 | 5,819 |
| `convnetjs/compile/build.xml` | 95 | 1,386 |
| `convnetjs/compile/yuicompressor-2.4.8.jar` | — | 787,524 |
| `convnetjs/demo/autoencoder.html` | 296 | 3,296 |
| `convnetjs/demo/automatic.html` | 927 | 9,324 |
| `convnetjs/demo/cifar10.html` | 547 | 6,101 |
| `convnetjs/demo/classify2d.html` | 380 | 3,297 |
| `convnetjs/demo/css/automatic.css` | 164 | 1,393 |
| `convnetjs/demo/css/style.css` | 200 | 1,446 |
| `convnetjs/demo/image_regression.html` | 396 | 3,608 |
| `convnetjs/demo/js/autoencoder.js` | 1,833 | 16,881 |
| `convnetjs/demo/js/automatic.js` | 1,299 | 11,401 |
| `convnetjs/demo/js/classify2d.js` | 1,164 | 9,853 |
| `convnetjs/demo/js/image-helpers.js` | 144 | 1,559 |
| `convnetjs/demo/js/image_regression.js` | 535 | 4,873 |
| `convnetjs/demo/js/images-demo.js` | 2,303 | 22,141 |
| `convnetjs/demo/js/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `convnetjs/demo/js/npgmain.js` | 412 | 3,311 |
| `convnetjs/demo/js/pica.js` | 2,844 | 20,897 |
| `convnetjs/demo/js/regression.js` | 389 | 3,848 |
| `convnetjs/demo/js/rldemo.js` | 2,071 | 19,309 |
| `convnetjs/demo/js/trainers.js` | 729 | 6,702 |
| `convnetjs/demo/mnist.html` | 542 | 5,951 |
| `convnetjs/demo/regression.html` | 257 | 2,738 |
| `convnetjs/demo/rldemo.html` | 861 | 158,456 |
| `convnetjs/demo/speedtest.html` | 143 | 1,226 |
| `convnetjs/demo/trainers.html` | 192 | 2,096 |
| `convnetjs/src/convnet_export.js` | 37 | 258 |
| `convnetjs/src/convnet_init.js` | 9 | 52 |
| `convnetjs/src/convnet_layers_dotproducts.js` | 1,156 | 10,425 |
| `convnetjs/src/convnet_layers_dropout.js` | 297 | 2,479 |
| `convnetjs/src/convnet_layers_input.js` | 136 | 1,209 |
| `convnetjs/src/convnet_layers_loss.js` | 915 | 6,904 |
| `convnetjs/src/convnet_layers_nonlinearities.js` | 995 | 8,183 |
| `convnetjs/src/convnet_layers_normalization.js` | 380 | 3,462 |
| `convnetjs/src/convnet_layers_pool.js` | 475 | 4,230 |
| `convnetjs/src/convnet_magicnet.js` | 1,300 | 11,824 |
| `convnetjs/src/convnet_net.js` | 805 | 7,593 |
| `convnetjs/src/convnet_trainers.js` | 933 | 7,413 |
| `convnetjs/src/convnet_util.js` | 503 | 3,644 |
| `convnetjs/src/convnet_vol.js` | 497 | 3,637 |
| `convnetjs/src/convnet_vol_util.js` | 397 | 2,981 |
| `convnetjs/test/jasmine/MIT.LICENSE` | 167 | 1,061 |
| `convnetjs/test/jasmine/SpecRunner.html` | 52 | 808 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/boot.js` | 739 | 6,133 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/console.js` | 514 | 4,318 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine-html.js` | 1,056 | 11,235 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.css` | 483 | 4,233 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine.js` | 6,569 | 62,835 |
| `convnetjs/test/jasmine/lib/jasmine-2.0.0/jasmine_favicon.png` | — | 2,057 |
| `convnetjs/test/jasmine/spec/NeuralNetSpec.js` | 343 | 2,945 |
| `covid-sanity/.gitignore` | 2 | 17 |
| `covid-sanity/LICENSE.md` | 171 | 1,081 |
| `covid-sanity/README.md` | 359 | 2,540 |
| `covid-sanity/banned.txt` | 9 | 140 |
| `covid-sanity/requirements.txt` | 5 | 34 |
| `covid-sanity/run.py` | 483 | 4,549 |
| `covid-sanity/serve.py` | 397 | 3,401 |
| `covid-sanity/static/favicon.png` | — | 10,792 |
| `covid-sanity/static/paper_list.js` | 222 | 2,207 |
| `covid-sanity/static/search.png` | — | 1,422 |
| `covid-sanity/static/style.css` | 333 | 2,864 |
| `covid-sanity/templates/index.html` | 171 | 2,080 |
| `covid-sanity/twitter_daemon.py` | 466 | 4,069 |
| `covid-sanity/ui.png` | — | 259,626 |
| `cryptos/.gitignore` | 2 | 32 |
| `cryptos/README.md` | 830 | 7,396 |
| `cryptos/blog.ipynb` | 14,517 | 104,850 |
| `cryptos/cryptos/__init__.py` | 0 | 0 |
| `cryptos/cryptos/bitcoin.py` | 90 | 1,200 |
| `cryptos/cryptos/block.py` | 414 | 3,962 |
| `cryptos/cryptos/curves.py` | 447 | 3,006 |
| `cryptos/cryptos/ecdsa.py` | 551 | 3,991 |
| `cryptos/cryptos/keys.py` | 681 | 5,305 |
| `cryptos/cryptos/network.py` | 1,226 | 11,344 |
| `cryptos/cryptos/ripemd160.py` | 2,936 | 13,019 |
| `cryptos/cryptos/sha256.py` | 775 | 5,303 |
| `cryptos/cryptos/transaction.py` | 1,733 | 16,294 |
| `cryptos/getnewaddress.py` | 85 | 804 |
| `cryptos/tests/__init__.py` | 0 | 0 |
| `cryptos/tests/test_block.py` | 211 | 3,090 |
| `cryptos/tests/test_ecdsa.py` | 301 | 2,802 |
| `cryptos/tests/test_hash.py` | 111 | 1,213 |
| `cryptos/tests/test_keys.py` | 258 | 3,502 |
| `cryptos/tests/test_network.py` | 140 | 2,596 |
| `cryptos/tests/test_tx.py` | 725 | 9,573 |
| `deep-vector-quantization/.gitignore` | 168 | 1,275 |
| `deep-vector-quantization/LICENSE` | 167 | 1,059 |
| `deep-vector-quantization/README.md` | 339 | 2,367 |
| `deep-vector-quantization/dvq/__init__.py` | 0 | 0 |
| `deep-vector-quantization/dvq/data/__init__.py` | 0 | 0 |
| `deep-vector-quantization/dvq/data/cifar10.py` | 98 | 1,510 |
| `deep-vector-quantization/dvq/model/__init__.py` | 0 | 0 |
| `deep-vector-quantization/dvq/model/deepmind_enc_dec.py` | 144 | 1,957 |
| `deep-vector-quantization/dvq/model/loss.py` | 205 | 1,569 |
| `deep-vector-quantization/dvq/model/openai_enc_dec.py` | 838 | 8,340 |
| `deep-vector-quantization/dvq/model/quantize.py` | 427 | 4,133 |
| `deep-vector-quantization/dvq/vqvae.py` | 890 | 9,214 |
| `deep-vector-quantization/requirements.txt` | 10 | 72 |
| `deep-vector-quantization/visualize.ipynb` | 392 | 360,309 |
| `find-birds/README.md` | 297 | 1,930 |
| `find-birds/common.py` | 216 | 2,002 |
| `find-birds/fetch.py` | 223 | 2,015 |
| `find-birds/report.py` | 551 | 4,642 |
| `find-birds/report_template.html` | 86 | 731 |
| `find-birds/requirements.txt` | 1 | 6 |
| `find-birds/ui.png` | — | 200,305 |
| `forestjs/MIT-LICENSE` | 167 | 1,059 |
| `forestjs/README.md` | 529 | 3,450 |
| `forestjs/demo/demoforest.html` | 878 | 7,735 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_diagonals-thick_18_b81900_40x40.png` | — | 260 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_diagonals-thick_20_666666_40x40.png` | — | 251 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_flat_10_000000_40x100.png` | — | 178 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_100_f6f6f6_1x400.png` | — | 104 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_100_fdf5ce_1x400.png` | — | 125 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_65_ffffff_1x400.png` | — | 105 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_gloss-wave_35_f6a828_500x100.png` | — | 4,427 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_highlight-soft_100_eeeeee_1x100.png` | — | 90 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-bg_highlight-soft_75_ffe45c_1x100.png` | — | 129 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-icons_222222_256x240.png` | — | 4,369 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-icons_228ef1_256x240.png` | — | 4,369 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ef8c08_256x240.png` | — | 4,369 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ffd27a_256x240.png` | — | 5,355 |
| `forestjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ffffff_256x240.png` | — | 4,369 |
| `forestjs/demo/jqueryui/css/ui-lightness/jquery-ui-1.8.21.custom.css` | 1,848 | 20,092 |
| `forestjs/demo/jqueryui/js/jquery-1.7.2.min.js` | 1,236 | 94,840 |
| `forestjs/demo/jqueryui/js/jquery-ui-1.8.21.custom.min.js` | 295 | 24,241 |
| `forestjs/demo/npg_include/npgmain.js` | 411 | 3,300 |
| `forestjs/demo/npg_include/vector2D.js` | 116 | 835 |
| `forestjs/lib/randomforest.js` | 1,391 | 11,809 |
| `gitstats/.gitignore` | 2 | 30 |
| `gitstats/README.md` | 105 | 579 |
| `gitstats/deploy/index.html` | 1,282 | 11,588 |
| `gitstats/deploy/jquery-3.3.1.min.js` | 1,283 | 86,927 |
| `gitstats/example_repos.json` | 18 | 329 |
| `gitstats/requirements.txt` | 1 | 9 |
| `gitstats/run.py` | 312 | 2,951 |
| `karpathy/README.md` | 5 | 25 |
| `lecun1989-repro/LICENSE` | 168 | 1,063 |
| `lecun1989-repro/README.md` | 1,019 | 5,984 |
| `lecun1989-repro/lecun1989.png` | — | 195,409 |
| `lecun1989-repro/modern.py` | 1,066 | 8,108 |
| `lecun1989-repro/prepro.py` | 211 | 1,578 |
| `lecun1989-repro/repro.py` | 770 | 6,382 |
| `lecun1989-repro/vis.ipynb` | 307 | 37,168 |
| `llama2.c/.github/workflows/build.yml` | 435 | 4,209 |
| `llama2.c/LICENSE` | 168 | 1,063 |
| `llama2.c/Makefile` | 346 | 2,330 |
| `llama2.c/README.md` | 5,037 | 35,271 |
| `llama2.c/assets/llama_cute.jpg` | — | 187,553 |
| `llama2.c/build_msvc.bat` | 7 | 45 |
| `llama2.c/configurator.py` | 219 | 1,758 |
| `llama2.c/doc/stories260K.md` | 459 | 2,909 |
| `llama2.c/doc/train_llama_tokenizer.md` | 378 | 3,532 |
| `llama2.c/export.py` | 2,160 | 24,513 |
| `llama2.c/model.py` | 1,587 | 15,289 |
| `llama2.c/requirements.txt` | 7 | 107 |
| `llama2.c/run.c` | 5,260 | 38,545 |
| `llama2.c/run.ipynb` | 317 | 3,981 |
| `llama2.c/runq.c` | 5,827 | 43,357 |
| `llama2.c/sample.py` | 382 | 3,397 |
| `llama2.c/test.c` | 433 | 3,574 |
| `llama2.c/test_all.py` | 406 | 3,748 |
| `llama2.c/tinystories.py` | 1,092 | 11,542 |
| `llama2.c/tokenizer.bin` | — | 433,869 |
| `llama2.c/tokenizer.model` | — | 499,723 |
| `llama2.c/tokenizer.py` | 304 | 2,866 |
| `llama2.c/train.py` | 1,671 | 13,915 |
| `llama2.c/win.c` | 459 | 4,269 |
| `llama2.c/win.h` | 209 | 1,612 |
| `llm-council/.gitignore` | 27 | 219 |
| `llm-council/.python-version` | 1 | 5 |
| `llm-council/CLAUDE.md` | 966 | 7,110 |
| `llm-council/README.md` | 489 | 3,135 |
| `llm-council/backend/__init__.py` | 4 | 35 |
| `llm-council/backend/config.py` | 62 | 628 |
| `llm-council/backend/council.py` | 1,182 | 10,528 |
| `llm-council/backend/main.py` | 545 | 6,836 |
| `llm-council/backend/openrouter.py` | 225 | 2,183 |
| `llm-council/backend/storage.py` | 395 | 4,430 |
| `llm-council/frontend/.gitignore` | 27 | 253 |
| `llm-council/frontend/README.md` | 113 | 1,157 |
| `llm-council/frontend/eslint.config.js` | 66 | 758 |
| `llm-council/frontend/index.html` | 28 | 357 |
| `llm-council/frontend/package-lock.json` | 6,682 | 136,497 |
| `llm-council/frontend/package.json` | 54 | 637 |
| `llm-council/frontend/public/vite.svg` | 90 | 1,497 |
| `llm-council/frontend/src/App.css` | 36 | 320 |
| `llm-council/frontend/src/App.jsx` | 515 | 6,044 |
| `llm-council/frontend/src/api.js` | 308 | 2,860 |
| `llm-council/frontend/src/assets/react.svg` | 366 | 4,126 |
| `llm-council/frontend/src/components/ChatInterface.css` | 298 | 2,607 |
| `llm-council/frontend/src/components/ChatInterface.jsx` | 321 | 4,457 |
| `llm-council/frontend/src/components/Sidebar.css` | 136 | 1,196 |
| `llm-council/frontend/src/components/Sidebar.jsx` | 87 | 1,215 |
| `llm-council/frontend/src/components/Stage1.css` | 120 | 964 |
| `llm-council/frontend/src/components/Stage1.jsx` | 83 | 1,008 |
| `llm-council/frontend/src/components/Stage2.css` | 278 | 2,240 |
| `llm-council/frontend/src/components/Stage2.jsx` | 260 | 3,341 |
| `llm-council/frontend/src/components/Stage3.css` | 42 | 370 |
| `llm-council/frontend/src/components/Stage3.jsx` | 48 | 621 |
| `llm-council/frontend/src/index.css` | 190 | 1,649 |
| `llm-council/frontend/src/main.jsx` | 24 | 229 |
| `llm-council/frontend/vite.config.js` | 18 | 161 |
| `llm-council/header.jpg` | — | 162,963 |
| `llm-council/main.py` | 10 | 89 |
| `llm-council/pyproject.toml` | 27 | 278 |
| `llm-council/start.sh` | 91 | 625 |
| `llm-council/uv.lock` | 6,773 | 141,673 |
| `llm.c/.github/workflows/ci.yml` | 755 | 9,440 |
| `llm.c/.github/workflows/ci_gpu.yml` | 419 | 3,638 |
| `llm.c/.github/workflows/ci_tests.yml` | 282 | 3,360 |
| `llm.c/.gitignore` | 46 | 518 |
| `llm.c/LICENSE` | 169 | 1,072 |
| `llm.c/Makefile` | 1,335 | 10,890 |
| `llm.c/README.md` | 2,278 | 16,471 |
| `llm.c/dev/cpu/matmul_forward.c` | 980 | 7,164 |
| `llm.c/dev/cuda/Makefile` | 328 | 3,328 |
| `llm.c/dev/cuda/README.md` | 377 | 2,347 |
| `llm.c/dev/cuda/adamw.cu` | 975 | 9,720 |
| `llm.c/dev/cuda/attention_backward.cu` | 6,860 | 49,193 |
| `llm.c/dev/cuda/attention_forward.cu` | 7,489 | 54,669 |
| `llm.c/dev/cuda/benchmark_on_modal.py` | 554 | 5,745 |
| `llm.c/dev/cuda/classifier_fused.cu` | 4,666 | 35,115 |
| `llm.c/dev/cuda/common.h` | 1,557 | 13,921 |
| `llm.c/dev/cuda/crossentropy_forward.cu` | 589 | 5,045 |
| `llm.c/dev/cuda/crossentropy_softmax_backward.cu` | 718 | 6,030 |
| `llm.c/dev/cuda/encoder_backward.cu` | 852 | 6,655 |
| `llm.c/dev/cuda/encoder_forward.cu` | 1,151 | 8,567 |
| `llm.c/dev/cuda/fused_residual_forward.cu` | 3,631 | 28,022 |
| `llm.c/dev/cuda/gelu_backward.cu` | 865 | 6,824 |
| `llm.c/dev/cuda/gelu_forward.cu` | 721 | 5,623 |
| `llm.c/dev/cuda/global_norm.cu` | 1,392 | 10,901 |
| `llm.c/dev/cuda/layernorm_backward.cu` | 8,938 | 71,946 |
| `llm.c/dev/cuda/layernorm_forward.cu` | 3,289 | 24,118 |
| `llm.c/dev/cuda/matmul_backward.cu` | 1,323 | 10,934 |
| `llm.c/dev/cuda/matmul_backward_bias.cu` | 3,623 | 27,255 |
| `llm.c/dev/cuda/matmul_forward.cu` | 2,151 | 18,230 |
| `llm.c/dev/cuda/nccl_all_reduce.cu` | 749 | 7,604 |
| `llm.c/dev/cuda/permute.cu` | 1,032 | 6,673 |
| `llm.c/dev/cuda/residual_forward.cu` | 638 | 5,418 |
| `llm.c/dev/cuda/softmax_forward.cu` | 3,669 | 25,050 |
| `llm.c/dev/cuda/trimat_forward.cu` | 4,459 | 27,483 |
| `llm.c/dev/data/README.md` | 120 | 741 |
| `llm.c/dev/data/data_common.py` | 576 | 4,908 |
| `llm.c/dev/data/edu_fineweb.sh` | 236 | 2,008 |
| `llm.c/dev/data/fineweb.py` | 636 | 6,286 |
| `llm.c/dev/data/fineweb.sh` | 238 | 1,992 |
| `llm.c/dev/data/hellaswag.py` | 861 | 7,646 |
| `llm.c/dev/data/mmlu.py` | 600 | 5,816 |
| `llm.c/dev/data/tinyshakespeare.py` | 398 | 4,068 |
| `llm.c/dev/data/tinystories.py` | 445 | 4,925 |
| `llm.c/dev/download_starter_pack.sh` | 217 | 2,046 |
| `llm.c/dev/eval/README.md` | 333 | 2,557 |
| `llm.c/dev/eval/export_hf.py` | 690 | 7,304 |
| `llm.c/dev/eval/run_eval.sh` | 312 | 4,899 |
| `llm.c/dev/eval/summarize_eval.py` | 102 | 1,074 |
| `llm.c/dev/loss_checker_ci.py` | 290 | 2,999 |
| `llm.c/dev/test/Makefile` | 747 | 5,737 |
| `llm.c/dev/test/device_file_io.cu` | 168 | 1,946 |
| `llm.c/dev/test/test_dataloader.c` | 1,521 | 11,929 |
| `llm.c/dev/test/test_outlier_detector.c` | 210 | 1,726 |
| `llm.c/dev/unistd.h` | 585 | 4,995 |
| `llm.c/dev/vislog.ipynb` | 620 | 5,702 |
| `llm.c/doc/layernorm/layernorm.c` | 917 | 6,204 |
| `llm.c/doc/layernorm/layernorm.md` | 2,914 | 18,425 |
| `llm.c/doc/layernorm/layernorm.py` | 303 | 1,996 |
| `llm.c/llmc/adamw.cuh` | 569 | 5,477 |
| `llm.c/llmc/attention.cuh` | 1,895 | 11,324 |
| `llm.c/llmc/cublas_common.h` | 131 | 1,306 |
| `llm.c/llmc/cuda_common.h` | 903 | 8,388 |
| `llm.c/llmc/cuda_utils.cuh` | 1,307 | 11,247 |
| `llm.c/llmc/cudnn_att.cpp` | 1,254 | 12,945 |
| `llm.c/llmc/cudnn_att.h` | 90 | 799 |
| `llm.c/llmc/dataloader.h` | 2,905 | 24,450 |
| `llm.c/llmc/encoder.cuh` | 1,541 | 11,302 |
| `llm.c/llmc/fused_classifier.cuh` | 905 | 6,800 |
| `llm.c/llmc/gelu.cuh` | 332 | 2,662 |
| `llm.c/llmc/global_norm.cuh` | 467 | 3,715 |
| `llm.c/llmc/layernorm.cuh` | 2,917 | 22,720 |
| `llm.c/llmc/logger.h` | 215 | 1,865 |
| `llm.c/llmc/matmul.cuh` | 1,450 | 14,117 |
| `llm.c/llmc/mfu.h` | 1,204 | 10,321 |
| `llm.c/llmc/outlier_detector.h` | 319 | 2,498 |
| `llm.c/llmc/rand.h` | 927 | 7,453 |
| `llm.c/llmc/sampler.h` | 175 | 1,146 |
| `llm.c/llmc/schedulers.h` | 449 | 4,340 |
| `llm.c/llmc/tokenizer.h` | 457 | 3,691 |
| `llm.c/llmc/utils.h` | 1,023 | 8,662 |
| `llm.c/llmc/zero.cuh` | 2,293 | 23,059 |
| `llm.c/profile_gpt2.cu` | 408 | 2,948 |
| `llm.c/profile_gpt2cu.py` | 1,021 | 8,682 |
| `llm.c/requirements.txt` | 7 | 59 |
| `llm.c/scripts/README.md` | 453 | 2,745 |
| `llm.c/scripts/multi_node/run_gpt2_124M_fs.sbatch` | 375 | 3,170 |
| `llm.c/scripts/multi_node/run_gpt2_124M_mpi.sh` | 210 | 1,579 |
| `llm.c/scripts/multi_node/run_gpt2_124M_tcp.sbatch` | 379 | 3,195 |
| `llm.c/scripts/pyrun_gpt2_124M.sh` | 103 | 876 |
| `llm.c/scripts/run_gpt2_124M.sh` | 176 | 1,289 |
| `llm.c/scripts/run_gpt2_1558M.sh` | 176 | 1,306 |
| `llm.c/scripts/run_gpt2_350M.sh` | 184 | 1,352 |
| `llm.c/scripts/run_gpt2_774M.sh` | 188 | 1,372 |
| `llm.c/scripts/run_gpt3_125M.sh` | 175 | 1,323 |
| `llm.c/test_gpt2.c` | 854 | 8,030 |
| `llm.c/test_gpt2.cu` | 1,968 | 17,190 |
| `llm.c/test_gpt2_fp32.cu` | 1,117 | 11,089 |
| `llm.c/train_gpt2.c` | 7,297 | 50,680 |
| `llm.c/train_gpt2.cu` | 12,396 | 104,649 |
| `llm.c/train_gpt2.py` | 4,516 | 41,860 |
| `llm.c/train_gpt2_fp32.cu` | 10,475 | 77,134 |
| `llm.c/train_llama3.py` | 5,729 | 57,539 |
| `llm101n/README.md` | 338 | 2,398 |
| `llm101n/llm101n.jpg` | — | 282,186 |
| `makemore/LICENSE` | 169 | 1,072 |
| `makemore/README.md` | 448 | 3,033 |
| `makemore/makemore.py` | 3,310 | 29,659 |
| `makemore/names.txt` | 32,033 | 228,145 |
| `micrograd/.gitignore` | 1 | 20 |
| `micrograd/LICENSE` | 171 | 1,081 |
| `micrograd/README.md` | 476 | 3,009 |
| `micrograd/demo.ipynb` | 1,306 | 57,550 |
| `micrograd/gout.svg` | 818 | 11,360 |
| `micrograd/micrograd/__init__.py` | 0 | 0 |
| `micrograd/micrograd/engine.py` | 317 | 2,730 |
| `micrograd/micrograd/nn.py` | 183 | 1,613 |
| `micrograd/moon_mlp.png` | — | 15,806 |
| `micrograd/puppy.jpg` | — | 49,269 |
| `micrograd/setup.py` | 56 | 717 |
| `micrograd/test/test_engine.py` | 304 | 1,470 |
| `micrograd/trace_graph.ipynb` | 321 | 2,934 |
| `minGPT/.gitignore` | 5 | 54 |
| `minGPT/LICENSE` | 171 | 1,081 |
| `minGPT/README.md` | 1,545 | 9,869 |
| `minGPT/demo.ipynb` | 1,318 | 11,266 |
| `minGPT/generate.ipynb` | 624 | 6,366 |
| `minGPT/mingpt.jpg` | — | 118,276 |
| `minGPT/mingpt/__init__.py` | 0 | 0 |
| `minGPT/mingpt/bpe.py` | 1,922 | 15,888 |
| `minGPT/mingpt/model.py` | 1,549 | 14,686 |
| `minGPT/mingpt/trainer.py` | 318 | 3,466 |
| `minGPT/mingpt/utils.py` | 412 | 3,596 |
| `minGPT/projects/adder/adder.py` | 1,011 | 8,287 |
| `minGPT/projects/adder/readme.md` | 10 | 53 |
| `minGPT/projects/chargpt/chargpt.py` | 396 | 4,079 |
| `minGPT/projects/chargpt/readme.md` | 84 | 687 |
| `minGPT/projects/readme.md` | 14 | 92 |
| `minGPT/setup.py` | 19 | 267 |
| `minGPT/tests/test_huggingface_import.py` | 190 | 2,057 |
| `minbpe/.gitignore` | 6 | 65 |
| `minbpe/LICENSE` | 168 | 1,063 |
| `minbpe/README.md` | 1,316 | 9,283 |
| `minbpe/assets/tiktokenizer.png` | — | 254,538 |
| `minbpe/exercise.md` | 517 | 3,605 |
| `minbpe/lecture.md` | 1,347 | 8,507 |
| `minbpe/minbpe/__init__.py` | 16 | 128 |
| `minbpe/minbpe/base.py` | 808 | 6,881 |
| `minbpe/minbpe/basic.py` | 367 | 2,883 |
| `minbpe/minbpe/gpt4.py` | 658 | 5,810 |
| `minbpe/minbpe/regex.py` | 840 | 7,344 |
| `minbpe/requirements.txt` | 2 | 14 |
| `minbpe/tests/__init__.py` | 0 | 0 |
| `minbpe/tests/taylorswift.txt` | 28,241 | 185,768 |
| `minbpe/tests/test_tokenizer.py` | 723 | 6,213 |
| `minbpe/train.py` | 116 | 882 |
| `nanoGPT/.gitattributes` | 20 | 214 |
| `nanoGPT/.gitignore` | 12 | 100 |
| `nanoGPT/LICENSE` | 169 | 1,072 |
| `nanoGPT/README.md` | 2,120 | 13,850 |
| `nanoGPT/assets/gpt2_124M_loss.png` | — | 110,433 |
| `nanoGPT/assets/nanogpt.jpg` | — | 118,621 |
| `nanoGPT/bench.py` | 487 | 4,815 |
| `nanoGPT/config/eval_gpt2.py` | 35 | 208 |
| `nanoGPT/config/eval_gpt2_large.py` | 35 | 215 |
| `nanoGPT/config/eval_gpt2_medium.py` | 35 | 216 |
| `nanoGPT/config/eval_gpt2_xl.py` | 35 | 213 |
| `nanoGPT/config/finetune_shakespeare.py` | 103 | 645 |
| `nanoGPT/config/train_gpt2.py` | 117 | 681 |
| `nanoGPT/config/train_shakespeare_char.py` | 196 | 1,132 |
| `nanoGPT/configurator.py` | 219 | 1,758 |
| `nanoGPT/data/openwebtext/prepare.py` | 377 | 3,167 |
| `nanoGPT/data/openwebtext/readme.md` | 47 | 489 |
| `nanoGPT/data/shakespeare/prepare.py` | 101 | 1,132 |
| `nanoGPT/data/shakespeare/readme.md` | 25 | 161 |
| `nanoGPT/data/shakespeare_char/prepare.py` | 286 | 2,344 |
| `nanoGPT/data/shakespeare_char/readme.md` | 29 | 209 |
| `nanoGPT/model.py` | 1,774 | 16,345 |
| `nanoGPT/sample.py` | 468 | 3,942 |
| `nanoGPT/scaling_laws.ipynb` | 3,295 | 268,519 |
| `nanoGPT/train.py` | 1,803 | 14,857 |
| `nanoGPT/transformer_sizing.ipynb` | 1,697 | 14,579 |
| `nanochat/.claude/skills/read-arxiv-paper/SKILL.md` | 317 | 1,973 |
| `nanochat/.gitignore` | 14 | 109 |
| `nanochat/.python-version` | 1 | 5 |
| `nanochat/LICENSE` | 169 | 1,072 |
| `nanochat/README.md` | 2,411 | 16,570 |
| `nanochat/dev/LEADERBOARD.md` | 1,941 | 12,993 |
| `nanochat/dev/LOG.md` | 9,232 | 63,385 |
| `nanochat/dev/estimate_gpt3_core.ipynb` | 6,955 | 73,112 |
| `nanochat/dev/nanochat.png` | — | 1,305 |
| `nanochat/dev/repackage_data_reference.py` | 516 | 4,580 |
| `nanochat/dev/scaling_analysis.ipynb` | 1,481 | 15,187 |
| `nanochat/dev/scaling_laws_jan26.png` | — | 93,061 |
| `nanochat/nanochat/__init__.py` | 0 | 0 |
| `nanochat/nanochat/checkpoint_manager.py` | 845 | 8,722 |
| `nanochat/nanochat/common.py` | 1,326 | 13,560 |
| `nanochat/nanochat/core_eval.py` | 1,259 | 11,572 |
| `nanochat/nanochat/dataloader.py` | 827 | 7,450 |
| `nanochat/nanochat/dataset.py` | 743 | 7,014 |
| `nanochat/nanochat/engine.py` | 1,539 | 15,533 |
| `nanochat/nanochat/execution.py` | 586 | 5,313 |
| `nanochat/nanochat/flash_attention.py` | 832 | 7,146 |
| `nanochat/nanochat/fp8.py` | 1,485 | 12,008 |
| `nanochat/nanochat/gpt.py` | 3,189 | 28,918 |
| `nanochat/nanochat/loss_eval.py` | 406 | 3,124 |
| `nanochat/nanochat/optim.py` | 2,549 | 23,314 |
| `nanochat/nanochat/tokenizer.py` | 1,235 | 12,911 |
| `nanochat/pyproject.toml` | 150 | 1,310 |
| `nanochat/runs/miniseries.sh` | 401 | 4,000 |
| `nanochat/runs/runcpu.sh` | 310 | 2,055 |
| `nanochat/runs/scaling_laws.sh` | 549 | 5,364 |
| `nanochat/runs/speedrun.sh` | 517 | 3,758 |
| `nanochat/scripts/base_eval.py` | 875 | 10,311 |
| `nanochat/scripts/base_train.py` | 3,483 | 32,313 |
| `nanochat/scripts/chat_cli.py` | 380 | 3,918 |
| `nanochat/scripts/chat_eval.py` | 1,135 | 11,557 |
| `nanochat/scripts/chat_rl.py` | 1,734 | 16,879 |
| `nanochat/scripts/chat_sft.py` | 2,554 | 24,733 |
| `nanochat/scripts/infer_bench.py` | 1,331 | 12,736 |
| `nanochat/scripts/tok_eval.py` | 1,270 | 11,127 |
| `nanochat/scripts/tok_train.py` | 384 | 3,730 |
| `nanochat/tasks/arc.py` | 235 | 2,159 |
| `nanochat/tasks/common.py` | 974 | 8,738 |
| `nanochat/tasks/gsm8k.py` | 526 | 4,861 |
| `nanochat/tasks/humaneval.py` | 381 | 3,537 |
| `nanochat/tasks/mmlu.py` | 312 | 3,552 |
| `nanochat/tasks/smoltalk.py` | 212 | 2,065 |
| `nanochat/tests/test_attention_fallback.py` | 1,497 | 16,095 |
| `nanochat/tests/test_engine.py` | 1,029 | 9,241 |
| `nanochat/tests/test_execution.py` | 249 | 2,513 |
| `nanochat/tests/test_optim.py` | 516 | 4,968 |
| `nanochat/tests/test_tasks.py` | 404 | 3,103 |
| `nanochat/tests/test_tokenizer.py` | 573 | 5,487 |
| `nanochat/uv.lock` | 25,752 | 473,535 |
| `neuraltalk/.gitignore` | 2 | 13 |
| `neuraltalk/Readme.md` | 1,177 | 7,758 |
| `neuraltalk/cv/Readme.md` | 6 | 39 |
| `neuraltalk/data/README.md` | 14 | 92 |
| `neuraltalk/driver.py` | 1,956 | 16,687 |
| `neuraltalk/eval/multi-bleu.perl` | 557 | 4,968 |
| `neuraltalk/eval_sentence_predictions.py` | 554 | 4,813 |
| `neuraltalk/example_images/7EGRMwN.jpg` | — | 281,335 |
| `neuraltalk/example_images/89pUfSc.jpg` | — | 162,122 |
| `neuraltalk/example_images/QmG3nS6.jpg` | — | 1,529,222 |
| `neuraltalk/example_images/Readme.md` | 284 | 1,728 |
| `neuraltalk/example_images/UbVIl1e.jpg` | — | 72,919 |
| `neuraltalk/example_images/animals.jpg` | — | 127,581 |
| `neuraltalk/example_images/cat.jpg` | — | 132,441 |
| `neuraltalk/example_images/cobra.jpg` | — | 90,383 |
| `neuraltalk/example_images/diving.jpg` | — | 591,412 |
| `neuraltalk/example_images/dogdinner.jpg` | — | 126,629 |
| `neuraltalk/example_images/frog.jpg` | — | 90,355 |
| `neuraltalk/example_images/gWEHGwf.jpg` | — | 245,278 |
| `neuraltalk/example_images/hole.jpg` | — | 57,550 |
| `neuraltalk/example_images/japanese.jpg` | — | 124,027 |
| `neuraltalk/example_images/jump.jpg` | — | 81,922 |
| `neuraltalk/example_images/koala.jpg` | — | 105,335 |
| `neuraltalk/example_images/mic.jpg` | — | 93,199 |
| `neuraltalk/example_images/pope.jpg` | — | 87,399 |
| `neuraltalk/example_images/pose.jpg` | — | 232,745 |
| `neuraltalk/example_images/qjujW6d.png` | — | 567,608 |
| `neuraltalk/example_images/result.html` | 210 | 1,643 |
| `neuraltalk/example_images/result_struct.json` | 326 | 3,037 |
| `neuraltalk/example_images/seal.jpg` | — | 42,311 |
| `neuraltalk/example_images/tasks.txt` | 16 | 170 |
| `neuraltalk/example_images/vgg_feats.mat` | — | 94,399 |
| `neuraltalk/example_images/work.jpg` | — | 230,247 |
| `neuraltalk/imagernn/Readme.md` | 129 | 841 |
| `neuraltalk/imagernn/__init__.py` | 0 | 0 |
| `neuraltalk/imagernn/data_provider.py` | 501 | 4,225 |
| `neuraltalk/imagernn/generic_batch_generator.py` | 719 | 5,701 |
| `neuraltalk/imagernn/imagernn_utils.py` | 218 | 1,718 |
| `neuraltalk/imagernn/lstm_generator.py` | 1,525 | 11,016 |
| `neuraltalk/imagernn/rnn_generator.py` | 1,319 | 9,572 |
| `neuraltalk/imagernn/solver.py` | 639 | 5,220 |
| `neuraltalk/imagernn/utils.py` | 123 | 804 |
| `neuraltalk/matlab_features_reference/README.md` | 119 | 756 |
| `neuraltalk/matlab_features_reference/deploy_features.prototxt` | 585 | 4,462 |
| `neuraltalk/matlab_features_reference/extract_features.m` | 149 | 1,250 |
| `neuraltalk/matlab_features_reference/prepare_images_batch.m` | 103 | 635 |
| `neuraltalk/monitorcv.html` | 452 | 4,280 |
| `neuraltalk/predict_on_images.py` | 500 | 4,029 |
| `neuraltalk/py_caffe_feat_extract.py` | 1,063 | 9,826 |
| `neuraltalk/python_features/README.md` | 85 | 614 |
| `neuraltalk/python_features/deploy_features.prototxt` | 585 | 4,462 |
| `neuraltalk/python_features/extract_features.py` | 346 | 3,347 |
| `neuraltalk/requirements.txt` | 3 | 21 |
| `neuraltalk/status/Readme.md` | 8 | 57 |
| `neuraltalk/vis_resources/d3.min.js` | 2,806 | 146,658 |
| `neuraltalk/vis_resources/d3utils.css` | 42 | 277 |
| `neuraltalk/vis_resources/d3utils.js` | 175 | 1,494 |
| `neuraltalk/vis_resources/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `neuraltalk/vis_resources/jsutils.js` | 117 | 809 |
| `neuraltalk/vis_resources/underscore-min.js` | 361 | 14,682 |
| `neuraltalk/vis_resources/underscore-min.map` | 3 | 25,382 |
| `neuraltalk/visualize_result_struct.html` | 470 | 5,025 |
| `neuraltalk2/.gitignore` | 8 | 95 |
| `neuraltalk2/README.md` | 1,763 | 12,220 |
| `neuraltalk2/coco-caption/myeval.py` | 143 | 1,154 |
| `neuraltalk2/coco/coco_preprocess.ipynb` | 575 | 5,216 |
| `neuraltalk2/convert_checkpoint_gpu_to_cpu.lua` | 409 | 3,682 |
| `neuraltalk2/cv/README.md` | 443 | 2,548 |
| `neuraltalk2/cv/driver.py` | 182 | 1,692 |
| `neuraltalk2/cv/inspect_cv.ipynb` | 953 | 181,144 |
| `neuraltalk2/cv/killall.sh` | 16 | 69 |
| `neuraltalk2/cv/runworker.sh` | 16 | 258 |
| `neuraltalk2/cv/spawn.sh` | 36 | 196 |
| `neuraltalk2/eval.lua` | 935 | 8,293 |
| `neuraltalk2/misc/DataLoader.lua` | 647 | 5,423 |
| `neuraltalk2/misc/DataLoaderRaw.lua` | 379 | 3,037 |
| `neuraltalk2/misc/LSTM.lua` | 248 | 2,187 |
| `neuraltalk2/misc/LanguageModel.lua` | 2,256 | 17,843 |
| `neuraltalk2/misc/call_python_caption_eval.sh` | 8 | 56 |
| `neuraltalk2/misc/gradcheck.lua` | 373 | 2,521 |
| `neuraltalk2/misc/net_utils.lua` | 868 | 6,776 |
| `neuraltalk2/misc/optim_updates.lua` | 275 | 2,281 |
| `neuraltalk2/misc/utils.lua` | 272 | 1,673 |
| `neuraltalk2/prepro.py` | 1,230 | 9,491 |
| `neuraltalk2/test_language_model.lua` | 1,157 | 10,583 |
| `neuraltalk2/train.lua` | 2,004 | 18,411 |
| `neuraltalk2/videocaptioning.lua` | 572 | 5,505 |
| `neuraltalk2/vis/imgs/dummy` | 0 | 0 |
| `neuraltalk2/vis/index.html` | 204 | 2,017 |
| `neuraltalk2/vis/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `neuraltalk2/vis/teaser.jpeg` | — | 40,873 |
| `ng-video-lecture/README.md` | 189 | 1,154 |
| `ng-video-lecture/bigram.py` | 523 | 4,140 |
| `ng-video-lecture/gpt.py` | 943 | 8,140 |
| `ng-video-lecture/input.txt` | 202,651 | 1,115,394 |
| `ng-video-lecture/more.txt` | 1,793 | 10,001 |
| `nipspreview/Readme.md` | 266 | 1,848 |
| `nipspreview/abstracts/dummy.txt` | 0 | 0 |
| `nipspreview/generatenice.py` | 244 | 1,873 |
| `nipspreview/generatenicelda.py` | 666 | 4,421 |
| `nipspreview/getabstracts.py` | 286 | 1,719 |
| `nipspreview/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `nipspreview/lda.py` | 606 | 5,993 |
| `nipspreview/makecorpus.py` | 224 | 1,384 |
| `nipspreview/nipsnice_template.html` | 929 | 7,125 |
| `nipspreview/pdftothumbs.py` | 170 | 1,045 |
| `nipspreview/pdftowordcloud.py` | 267 | 1,632 |
| `nipspreview/scrape.py` | 305 | 2,126 |
| `nipspreview/stopwords.txt` | 668 | 4,180 |
| `nipspreview/thumbs/dummy.txt` | 0 | 0 |
| `nipspreview/vocabulary.py` | 302 | 6,612 |
| `nn-zero-to-hero/LICENSE` | 169 | 1,072 |
| `nn-zero-to-hero/README.md` | 917 | 6,828 |
| `nn-zero-to-hero/lectures/makemore/makemore_part1_bigrams.ipynb` | 6,056 | 389,057 |
| `nn-zero-to-hero/lectures/makemore/makemore_part2_mlp.ipynb` | 1,441 | 47,747 |
| `nn-zero-to-hero/lectures/makemore/makemore_part3_bn.ipynb` | 3,408 | 495,080 |
| `nn-zero-to-hero/lectures/makemore/makemore_part4_backprop.ipynb` | 3,500 | 37,502 |
| `nn-zero-to-hero/lectures/makemore/makemore_part5_cnn1.ipynb` | 1,986 | 35,882 |
| `nn-zero-to-hero/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb` | 4,055 | 81,042 |
| `nn-zero-to-hero/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb` | 4,434 | 76,357 |
| `nn/.luacheckrc` | 21 | 149 |
| `nn/.travis.yml` | 118 | 1,063 |
| `nn/Abs.lua` | 26 | 342 |
| `nn/AbsCriterion.lua` | 29 | 410 |
| `nn/Add.lua` | 139 | 1,699 |
| `nn/AddConstant.lua` | 83 | 984 |
| `nn/BCECriterion.lua` | 116 | 1,584 |
| `nn/BatchNormalization.lua` | 530 | 5,792 |
| `nn/CAddTable.lua` | 41 | 580 |
| `nn/CDivTable.lua` | 38 | 667 |
| `nn/CMakeLists.txt` | 167 | 1,833 |
| `nn/CMul.lua` | 275 | 3,574 |
| `nn/CMulTable.lua` | 73 | 1,083 |
| `nn/CONTRIBUTING.md` | 727 | 4,983 |
| `nn/COPYRIGHT.txt` | 289 | 2,049 |
| `nn/CSubTable.lua` | 38 | 618 |
| `nn/ClassNLLCriterion.lua` | 260 | 2,966 |
| `nn/Concat.lua` | 399 | 3,881 |
| `nn/ConcatTable.lua` | 353 | 3,268 |
| `nn/Container.lua` | 148 | 1,717 |
| `nn/Copy.lua` | 89 | 1,142 |
| `nn/CosineDistance.lua` | 84 | 1,079 |
| `nn/CosineEmbeddingCriterion.lua` | 121 | 1,328 |
| `nn/Criterion.lua` | 112 | 1,247 |
| `nn/CriterionTable.lua` | 31 | 504 |
| `nn/CrossEntropyCriterion.lua` | 70 | 951 |
| `nn/DepthConcat.lua` | 430 | 4,471 |
| `nn/DistKLDivCriterion.lua` | 29 | 454 |
| `nn/DotProduct.lua` | 49 | 652 |
| `nn/Dropout.lua` | 111 | 1,119 |
| `nn/ErrorMessages.lua` | 41 | 322 |
| `nn/Euclidean.lua` | 489 | 5,685 |
| `nn/Exp.lua` | 17 | 224 |
| `nn/FlattenTable.lua` | 421 | 3,118 |
| `nn/HardShrink.lua` | 31 | 422 |
| `nn/HardTanh.lua` | 19 | 281 |
| `nn/HingeEmbeddingCriterion.lua` | 66 | 666 |
| `nn/Identity.lua` | 23 | 263 |
| `nn/Jacobian.lua` | 660 | 8,186 |
| `nn/JoinTable.lua` | 153 | 1,830 |
| `nn/L1Cost.lua` | 19 | 307 |
| `nn/L1HingeEmbeddingCriterion.lua` | 101 | 1,160 |
| `nn/L1Penalty.lua` | 113 | 1,129 |
| `nn/L2Normalize.lua` | 144 | 1,597 |
| `nn/Linear.lua` | 268 | 3,191 |
| `nn/Log.lua` | 28 | 458 |
| `nn/LogSigmoid.lua` | 27 | 390 |
| `nn/LogSoftMax.lua` | 19 | 293 |
| `nn/LookupTable.lua` | 447 | 4,662 |
| `nn/MM.lua` | 326 | 2,695 |
| `nn/MSECriterion.lua` | 29 | 410 |
| `nn/MarginCriterion.lua` | 35 | 484 |
| `nn/MarginRankingCriterion.lua` | 133 | 1,963 |
| `nn/Max.lua` | 35 | 411 |
| `nn/Mean.lua` | 72 | 959 |
| `nn/Min.lua` | 35 | 411 |
| `nn/MixtureTable.lua` | 386 | 5,277 |
| `nn/Module.lua` | 732 | 8,166 |
| `nn/Mul.lua` | 68 | 860 |
| `nn/MulConstant.lua` | 85 | 1,071 |
| `nn/MultiCriterion.lua` | 81 | 1,095 |
| `nn/MultiLabelMarginCriterion.lua` | 29 | 501 |
| `nn/MultiMarginCriterion.lua` | 58 | 609 |
| `nn/Narrow.lua` | 43 | 713 |
| `nn/PReLU.lua` | 68 | 825 |
| `nn/Padding.lua` | 137 | 1,441 |
| `nn/PairwiseDistance.lua` | 199 | 2,674 |
| `nn/Parallel.lua` | 338 | 3,780 |
| `nn/ParallelCriterion.lua` | 123 | 1,687 |
| `nn/ParallelTable.lua` | 213 | 1,694 |
| `nn/Power.lua` | 36 | 549 |
| `nn/README.md` | 202 | 2,638 |
| `nn/ReLU.lua` | 10 | 118 |
| `nn/Replicate.lua` | 160 | 1,470 |
| `nn/Reshape.lua` | 158 | 1,801 |
| `nn/Select.lua` | 35 | 562 |
| `nn/SelectTable.lua` | 94 | 1,016 |
| `nn/Sequential.lua` | 326 | 3,488 |
| `nn/Sigmoid.lua` | 19 | 275 |
| `nn/SoftMax.lua` | 20 | 278 |
| `nn/SoftMin.lua` | 36 | 557 |
| `nn/SoftPlus.lua` | 87 | 762 |
| `nn/SoftShrink.lua` | 31 | 422 |
| `nn/SoftSign.lua` | 30 | 561 |
| `nn/SparseJacobian.lua` | 696 | 8,618 |
| `nn/SparseLinear.lua` | 130 | 1,740 |
| `nn/SpatialAdaptiveMaxPooling.lua` | 45 | 799 |
| `nn/SpatialAveragePooling.lua` | 84 | 906 |
| `nn/SpatialBatchNormalization.lua` | 662 | 7,239 |
| `nn/SpatialContrastiveNormalization.lua` | 118 | 1,444 |
| `nn/SpatialConvolution.lua` | 334 | 3,794 |
| `nn/SpatialConvolutionMM.lua` | 201 | 2,450 |
| `nn/SpatialConvolutionMap.lua` | 446 | 4,530 |
| `nn/SpatialDivisiveNormalization.lua` | 326 | 4,659 |
| `nn/SpatialDropout.lua` | 132 | 1,350 |
| `nn/SpatialFullConvolution.lua` | 127 | 1,589 |
| `nn/SpatialFullConvolutionMap.lua` | 143 | 1,990 |
| `nn/SpatialLPPooling.lua` | 101 | 959 |
| `nn/SpatialMaxPooling.lua` | 63 | 816 |
| `nn/SpatialSubSampling.lua` | 115 | 1,412 |
| `nn/SpatialSubtractiveNormalization.lua` | 258 | 3,302 |
| `nn/SpatialUpSamplingNearest.lua` | 198 | 1,974 |
| `nn/SpatialZeroPadding.lua` | 708 | 5,655 |
| `nn/SplitTable.lua` | 89 | 1,055 |
| `nn/Sqrt.lua` | 30 | 362 |
| `nn/Square.lua` | 23 | 333 |
| `nn/StochasticGradient.lua` | 173 | 1,921 |
| `nn/Sum.lua` | 81 | 858 |
| `nn/Tanh.lua` | 19 | 257 |
| `nn/TanhShrink.lua` | 35 | 555 |
| `nn/TemporalConvolution.lua` | 125 | 1,670 |
| `nn/TemporalMaxPooling.lua` | 50 | 767 |
| `nn/TemporalSubSampling.lua` | 102 | 1,378 |
| `nn/Threshold.lua` | 118 | 1,158 |
| `nn/Transpose.lua` | 66 | 754 |
| `nn/View.lua` | 261 | 2,232 |
| `nn/VolumetricConvolution.lua` | 148 | 1,702 |
| `nn/VolumetricMaxPooling.lua` | 76 | 897 |
| `nn/WeightedEuclidean.lua` | 644 | 8,147 |
| `nn/WeightedMSECriterion.lua` | 62 | 894 |
| `nn/doc/containers.md` | 1,020 | 8,376 |
| `nn/doc/convolution.md` | 3,364 | 23,216 |
| `nn/doc/criterion.md` | 2,545 | 19,343 |
| `nn/doc/image/abs.png` | — | 5,918 |
| `nn/doc/image/exp.png` | — | 6,104 |
| `nn/doc/image/hshrink.png` | — | 5,576 |
| `nn/doc/image/htanh.png` | — | 5,948 |
| `nn/doc/image/lena.jpg` | — | 39,706 |
| `nn/doc/image/lenap.jpg` | — | 34,838 |
| `nn/doc/image/logsigmoid.png` | — | 9,116 |
| `nn/doc/image/logsoftmax.png` | — | 8,712 |
| `nn/doc/image/power.png` | — | 6,515 |
| `nn/doc/image/prelu.png` | — | 19,812 |
| `nn/doc/image/relu.png` | — | 19,636 |
| `nn/doc/image/sigmmoid.png` | — | 6,533 |
| `nn/doc/image/sigmoid.png` | — | 6,533 |
| `nn/doc/image/softmax.png` | — | 6,252 |
| `nn/doc/image/softmin.png` | — | 6,446 |
| `nn/doc/image/softplus.png` | — | 9,375 |
| `nn/doc/image/softsign.png` | — | 6,877 |
| `nn/doc/image/sqrt.png` | — | 6,008 |
| `nn/doc/image/square.png` | — | 6,984 |
| `nn/doc/image/sshrink.png` | — | 5,576 |
| `nn/doc/image/tanh.png` | — | 7,323 |
| `nn/doc/module.md` | 1,701 | 13,613 |
| `nn/doc/overview.md` | 901 | 7,364 |
| `nn/doc/simple.md` | 3,898 | 28,249 |
| `nn/doc/table.md` | 3,370 | 25,610 |
| `nn/doc/testing.md` | 42 | 328 |
| `nn/doc/training.md` | 973 | 7,387 |
| `nn/doc/transfer.md` | 868 | 7,837 |
| `nn/generic/Abs.c` | 117 | 1,254 |
| `nn/generic/AbsCriterion.c` | 146 | 1,607 |
| `nn/generic/DistKLDivCriterion.c` | 153 | 1,699 |
| `nn/generic/HardShrink.c` | 151 | 1,629 |
| `nn/generic/HardTanh.c` | 251 | 2,572 |
| `nn/generic/L1Cost.c` | 111 | 1,248 |
| `nn/generic/LogSigmoid.c` | 138 | 1,602 |
| `nn/generic/LogSoftMax.c` | 335 | 3,059 |
| `nn/generic/MSECriterion.c` | 145 | 1,619 |
| `nn/generic/MarginCriterion.c` | 167 | 1,809 |
| `nn/generic/Max.c` | 277 | 3,336 |
| `nn/generic/Min.c` | 277 | 3,336 |
| `nn/generic/MultiLabelMarginCriterion.c` | 513 | 5,032 |
| `nn/generic/MultiMarginCriterion.c` | 447 | 4,233 |
| `nn/generic/PReLU.c` | 711 | 6,215 |
| `nn/generic/Sigmoid.c` | 118 | 1,293 |
| `nn/generic/SoftMax.c` | 312 | 2,705 |
| `nn/generic/SoftPlus.c` | 196 | 1,931 |
| `nn/generic/SoftShrink.c` | 155 | 1,647 |
| `nn/generic/SparseLinear.c` | 1,037 | 10,175 |
| `nn/generic/SpatialAdaptiveMaxPooling.c` | 830 | 9,345 |
| `nn/generic/SpatialAveragePooling.c` | 591 | 5,276 |
| `nn/generic/SpatialConvolution.c` | 652 | 6,312 |
| `nn/generic/SpatialConvolutionMM.c` | 1,308 | 14,346 |
| `nn/generic/SpatialConvolutionMap.c` | 905 | 8,866 |
| `nn/generic/SpatialFullConvolution.c` | 666 | 6,405 |
| `nn/generic/SpatialFullConvolutionMap.c` | 771 | 7,941 |
| `nn/generic/SpatialMaxPooling.c` | 834 | 8,769 |
| `nn/generic/SpatialSubSampling.c` | 924 | 8,340 |
| `nn/generic/SpatialUpSamplingNearest.c` | 551 | 4,430 |
| `nn/generic/Sqrt.c` | 228 | 2,401 |
| `nn/generic/Square.c` | 196 | 2,114 |
| `nn/generic/Tanh.c` | 206 | 2,159 |
| `nn/generic/TemporalConvolution.c` | 953 | 12,641 |
| `nn/generic/TemporalMaxPooling.c` | 760 | 6,611 |
| `nn/generic/TemporalSubSampling.c` | 379 | 4,443 |
| `nn/generic/Threshold.c` | 198 | 2,224 |
| `nn/generic/VolumetricConvolution.c` | 707 | 6,928 |
| `nn/generic/VolumetricMaxPooling.c` | 1,087 | 9,680 |
| `nn/hessian.lua` | 1,031 | 17,742 |
| `nn/init.c` | 268 | 5,800 |
| `nn/init.lua` | 121 | 3,350 |
| `nn/rocks/nn-scm-1.rockspec` | 74 | 561 |
| `nn/test.lua` | 13,876 | 139,533 |
| `nn/utils.lua` | 45 | 471 |
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
| `pytorch-made/README.md` | 453 | 2,911 |
| `pytorch-made/made.png` | — | 79,759 |
| `pytorch-made/made.py` | 670 | 5,973 |
| `pytorch-made/run.py` | 395 | 3,983 |
| `pytorch-normalizing-flows/Readme.md` | 76 | 593 |
| `pytorch-normalizing-flows/assets/moon_flow.png` | — | 110,381 |
| `pytorch-normalizing-flows/nflib/__init__.py` | 0 | 0 |
| `pytorch-normalizing-flows/nflib/flows.py` | 1,231 | 10,318 |
| `pytorch-normalizing-flows/nflib/made.py` | 477 | 4,200 |
| `pytorch-normalizing-flows/nflib/nets.py` | 241 | 2,287 |
| `pytorch-normalizing-flows/nflib/spline_flows.py` | 1,200 | 10,940 |
| `pytorch-normalizing-flows/nflib1.ipynb` | 1,827 | 815,336 |
| `randomfun/MicroGrad.ipynb` | 95 | 1,023 |
| `randomfun/MixtureDensityNets.ipynb` | 2,808 | 295,720 |
| `randomfun/README.md` | 12 | 72 |
| `randomfun/es.ipynb` | 443 | 94,291 |
| `randomfun/floats.ipynb` | 2,539 | 34,912 |
| `randomfun/irust/hello-rust/Cargo.toml` | 23 | 199 |
| `randomfun/irust/hello-rust/src/main.rs` | 835 | 6,397 |
| `randomfun/irust/readme.md` | 127 | 923 |
| `randomfun/knn_vs_svm.ipynb` | 716 | 5,802 |
| `randomfun/lectures/makemore/makemore_part1_bigrams.ipynb` | 6,056 | 389,057 |
| `randomfun/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb` | 4,055 | 81,042 |
| `randomfun/lectures/micrograd/micrograd_lecture_second_half_roughly.ipynb` | 4,434 | 76,357 |
| `randomfun/min-char-rnn-nb.ipynb` | 2,167 | 18,906 |
| `randomfun/min-char-rnn-nb2.ipynb` | 2,761 | 24,154 |
| `randomfun/min-char-rnn-nb3.ipynb` | 3,047 | 26,470 |
| `randomfun/nand_to_uint.ipynb` | 11,079 | 187,088 |
| `randomfun/puppy.jpg` | — | 30,452 |
| `randomfun/rnnlm.jpeg` | — | 84,774 |
| `randomfun/sexual_reproduction.ipynb` | 903 | 25,661 |
| `randomfun/transformer_unify.ipynb` | 640 | 5,143 |
| `recurrentjs/Readme.md` | 770 | 4,590 |
| `recurrentjs/character_demo.html` | 18,412 | 107,846 |
| `recurrentjs/external/images/ui-bg_diagonals-thick_18_b81900_40x40.png` | — | 418 |
| `recurrentjs/external/images/ui-bg_diagonals-thick_20_666666_40x40.png` | — | 312 |
| `recurrentjs/external/images/ui-bg_flat_10_000000_40x100.png` | — | 205 |
| `recurrentjs/external/images/ui-bg_glass_100_f6f6f6_1x400.png` | — | 262 |
| `recurrentjs/external/images/ui-bg_glass_100_fdf5ce_1x400.png` | — | 348 |
| `recurrentjs/external/images/ui-bg_glass_65_ffffff_1x400.png` | — | 207 |
| `recurrentjs/external/images/ui-bg_gloss-wave_35_f6a828_500x100.png` | — | 5,815 |
| `recurrentjs/external/images/ui-bg_highlight-soft_100_eeeeee_1x100.png` | — | 278 |
| `recurrentjs/external/images/ui-bg_highlight-soft_75_ffe45c_1x100.png` | — | 328 |
| `recurrentjs/external/images/ui-icons_222222_256x240.png` | — | 6,922 |
| `recurrentjs/external/images/ui-icons_228ef1_256x240.png` | — | 4,549 |
| `recurrentjs/external/images/ui-icons_ef8c08_256x240.png` | — | 4,549 |
| `recurrentjs/external/images/ui-icons_ffd27a_256x240.png` | — | 4,549 |
| `recurrentjs/external/images/ui-icons_ffffff_256x240.png` | — | 6,299 |
| `recurrentjs/external/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `recurrentjs/external/jquery-ui.min.css` | 350 | 18,195 |
| `recurrentjs/external/jquery-ui.min.js` | 543 | 100,680 |
| `recurrentjs/src/recurrent.js` | 1,990 | 15,861 |
| `recurrentjs/src/vis.js` | 293 | 2,420 |
| `reinforcejs/README.md` | 261 | 1,936 |
| `reinforcejs/agentzoo/puckagent.json` | 1 | 36,359 |
| `reinforcejs/agentzoo/wateragent.json` | 1 | 446,607 |
| `reinforcejs/external/.DS_Store` | — | 6,148 |
| `reinforcejs/external/d3.min.js` | 2,892 | 150,762 |
| `reinforcejs/external/highlight.pack.js` | 289 | 10,183 |
| `reinforcejs/external/highlight_default.css` | 239 | 2,642 |
| `reinforcejs/external/images/ui-bg_diagonals-thick_18_b81900_40x40.png` | — | 418 |
| `reinforcejs/external/images/ui-bg_diagonals-thick_20_666666_40x40.png` | — | 312 |
| `reinforcejs/external/images/ui-bg_flat_10_000000_40x100.png` | — | 205 |
| `reinforcejs/external/images/ui-bg_glass_100_f6f6f6_1x400.png` | — | 262 |
| `reinforcejs/external/images/ui-bg_glass_100_fdf5ce_1x400.png` | — | 348 |
| `reinforcejs/external/images/ui-bg_glass_65_ffffff_1x400.png` | — | 207 |
| `reinforcejs/external/images/ui-bg_gloss-wave_35_f6a828_500x100.png` | — | 5,815 |
| `reinforcejs/external/images/ui-bg_highlight-soft_100_eeeeee_1x100.png` | — | 278 |
| `reinforcejs/external/images/ui-bg_highlight-soft_75_ffe45c_1x100.png` | — | 328 |
| `reinforcejs/external/images/ui-icons_222222_256x240.png` | — | 6,922 |
| `reinforcejs/external/images/ui-icons_228ef1_256x240.png` | — | 4,549 |
| `reinforcejs/external/images/ui-icons_ef8c08_256x240.png` | — | 4,549 |
| `reinforcejs/external/images/ui-icons_ffd27a_256x240.png` | — | 4,549 |
| `reinforcejs/external/images/ui-icons_ffffff_256x240.png` | — | 6,299 |
| `reinforcejs/external/jquery-1.11.2.min.js` | 1,412 | 95,931 |
| `reinforcejs/external/jquery-2.1.3.min.js` | 1,304 | 84,319 |
| `reinforcejs/external/jquery-ui.min.css` | 350 | 18,195 |
| `reinforcejs/external/jquery-ui.min.js` | 543 | 100,680 |
| `reinforcejs/external/jquery.flot.min.js` | 490 | 52,966 |
| `reinforcejs/external/marked.js` | 3,150 | 28,191 |
| `reinforcejs/external/mathjax.js` | 934 | 60,573 |
| `reinforcejs/external/underscore-min.js` | 388 | 16,523 |
| `reinforcejs/gridworld_dp.html` | 3,381 | 26,862 |
| `reinforcejs/gridworld_td.html` | 4,341 | 34,259 |
| `reinforcejs/img/dpsolved.jpeg` | — | 49,769 |
| `reinforcejs/img/lambda.png` | — | 11,661 |
| `reinforcejs/img/policyiter.png` | — | 8,654 |
| `reinforcejs/img/qsa.jpeg` | — | 44,553 |
| `reinforcejs/img/sarsa.png` | — | 4,543 |
| `reinforcejs/img/traces.png` | — | 8,979 |
| `reinforcejs/index.html` | 712 | 6,873 |
| `reinforcejs/lib/rl.js` | 6,184 | 48,146 |
| `reinforcejs/loop.svg` | 52 | 1,293 |
| `reinforcejs/puckworld.html` | 3,779 | 30,181 |
| `reinforcejs/waterworld.html` | 1,497 | 16,148 |
| `reinforcejs/waterworld.js` | 1,590 | 12,343 |
| `researchlei/Readme.md` | 597 | 3,957 |
| `researchlei/addpaper.py` | 938 | 7,013 |
| `researchlei/client/arrowdown.png` | — | 3,383 |
| `researchlei/client/arrowup.png` | — | 2,843 |
| `researchlei/client/authors.html` | 481 | 4,854 |
| `researchlei/client/back.png` | — | 2,399 |
| `researchlei/client/bulb.png` | — | 1,317 |
| `researchlei/client/d3.v3.min.js` | 2,545 | 137,385 |
| `researchlei/client/graph.png` | — | 4,767 |
| `researchlei/client/index.html` | 1,553 | 14,959 |
| `researchlei/client/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `researchlei/client/style.css` | 423 | 3,310 |
| `researchlei/copyresources.py` | 140 | 1,035 |
| `researchlei/genjson.py` | 221 | 1,826 |
| `researchlei/stopwords.txt` | 668 | 4,180 |
| `researchlei/topwords.py` | 223 | 1,471 |
| `researchpooler/README` | 1,067 | 7,540 |
| `researchpooler/demo1.py` | 203 | 1,477 |
| `researchpooler/demo2.py` | 143 | 1,071 |
| `researchpooler/demo3.py` | 271 | 2,095 |
| `researchpooler/google_search.py` | 115 | 922 |
| `researchpooler/nips_add_pdftext.py` | 217 | 1,864 |
| `researchpooler/nips_download_parse.py` | 446 | 4,474 |
| `researchpooler/pdf_read.py` | 126 | 1,096 |
| `researchpooler/repool_analysis.py` | 154 | 1,305 |
| `researchpooler/repool_util.py` | 274 | 2,111 |
| `scholaroctopus/README.md` | 132 | 906 |
| `scholaroctopus/render/d3.min.js` | 2,806 | 146,658 |
| `scholaroctopus/render/data5.json` | 189,570 | 2,303,455 |
| `scholaroctopus/render/icon.svg` | 2,402 | 29,397 |
| `scholaroctopus/render/index.html` | 1,301 | 12,169 |
| `scholaroctopus/render/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `svmjs/MIT-LICENSE` | 167 | 1,059 |
| `svmjs/README.md` | 659 | 4,008 |
| `svmjs/demo/demosvm.html` | 877 | 8,164 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_diagonals-thick_18_b81900_40x40.png` | — | 260 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_diagonals-thick_20_666666_40x40.png` | — | 251 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_flat_10_000000_40x100.png` | — | 178 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_100_f6f6f6_1x400.png` | — | 104 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_100_fdf5ce_1x400.png` | — | 125 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_glass_65_ffffff_1x400.png` | — | 105 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_gloss-wave_35_f6a828_500x100.png` | — | 4,427 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_highlight-soft_100_eeeeee_1x100.png` | — | 90 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-bg_highlight-soft_75_ffe45c_1x100.png` | — | 129 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-icons_222222_256x240.png` | — | 4,369 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-icons_228ef1_256x240.png` | — | 4,369 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ef8c08_256x240.png` | — | 4,369 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ffd27a_256x240.png` | — | 5,355 |
| `svmjs/demo/jqueryui/css/ui-lightness/images/ui-icons_ffffff_256x240.png` | — | 4,369 |
| `svmjs/demo/jqueryui/css/ui-lightness/jquery-ui-1.8.21.custom.css` | 1,848 | 20,092 |
| `svmjs/demo/jqueryui/js/jquery-1.7.2.min.js` | 1,236 | 94,840 |
| `svmjs/demo/jqueryui/js/jquery-ui-1.8.21.custom.min.js` | 295 | 24,241 |
| `svmjs/demo/npg_include/npgmain.js` | 411 | 3,300 |
| `svmjs/demo/npg_include/vector2D.js` | 116 | 835 |
| `svmjs/lib/svm.js` | 1,463 | 12,268 |
| `svmjs/package.json` | 31 | 344 |
| `svmjs/test/smo.pdf` | — | 79,701 |
| `svmjs/test/testnode.js` | 69 | 717 |
| `svmjs/test/testsvm.html` | 276 | 2,446 |
| `svmjs/test/testsvm.m` | 146 | 1,023 |
| `tf-agent/README.md` | 10 | 55 |
| `tf-agent/policy_gradient.py` | 619 | 6,333 |
| `transformers/.circleci/TROUBLESHOOT.md` | 45 | 321 |
| `transformers/.circleci/config.yml` | 3,356 | 43,769 |
| `transformers/.coveragerc` | 23 | 207 |
| `transformers/.gitattributes` | 8 | 51 |
| `transformers/.github/ISSUE_TEMPLATE/bug-report.yml` | 512 | 4,732 |
| `transformers/.github/ISSUE_TEMPLATE/config.yml` | 63 | 529 |
| `transformers/.github/ISSUE_TEMPLATE/feature-request.yml` | 134 | 1,100 |
| `transformers/.github/ISSUE_TEMPLATE/migration.yml` | 292 | 2,730 |
| `transformers/.github/ISSUE_TEMPLATE/new-model-addition.yml` | 133 | 1,077 |
| `transformers/.github/PULL_REQUEST_TEMPLATE.md` | 424 | 3,074 |
| `transformers/.github/conda/build.sh` | 10 | 69 |
| `transformers/.github/conda/meta.yaml` | 116 | 978 |
| `transformers/.github/workflows/TROUBLESHOOT.md` | 49 | 384 |
| `transformers/.github/workflows/add-model-like.yml` | 255 | 2,514 |
| `transformers/.github/workflows/build-docker-images.yml` | 421 | 5,396 |
| `transformers/.github/workflows/build_documentation.yml` | 37 | 432 |
| `transformers/.github/workflows/build_pr_documentation.yml` | 37 | 434 |
| `transformers/.github/workflows/delete_doc_comment.yml` | 21 | 254 |
| `transformers/.github/workflows/doctests.yml` | 191 | 2,234 |
| `transformers/.github/workflows/model-templates.yml` | 283 | 3,722 |
| `transformers/.github/workflows/release-conda.yml` | 100 | 1,078 |
| `transformers/.github/workflows/self-nightly-scheduled.yml` | 807 | 9,160 |
| `transformers/.github/workflows/self-push-caller.yml` | 129 | 1,371 |
| `transformers/.github/workflows/self-push.yml` | 2,167 | 22,500 |
| `transformers/.github/workflows/self-scheduled.yml` | 1,155 | 13,285 |
| `transformers/.github/workflows/stale.yml` | 60 | 552 |
| `transformers/.github/workflows/update_metdata.yml` | 96 | 1,034 |
| `transformers/.gitignore` | 231 | 1,780 |
| `transformers/CITATION.cff` | 231 | 2,331 |
| `transformers/CODE_OF_CONDUCT.md` | 710 | 5,226 |
| `transformers/CONTRIBUTING.md` | 2,454 | 16,242 |
| `transformers/ISSUES.md` | 2,990 | 18,855 |
| `transformers/LICENSE` | 1,590 | 11,418 |
| `transformers/MANIFEST.in` | 2 | 16 |
| `transformers/Makefile` | 361 | 3,302 |
| `transformers/README.md` | 5,923 | 60,707 |
| `transformers/README_ko.md` | 5,430 | 60,608 |
| `transformers/README_zh-hans.md` | 4,625 | 59,181 |
| `transformers/README_zh-hant.md` | 4,962 | 59,602 |
| `transformers/conftest.py` | 328 | 2,846 |
| `transformers/docker/transformers-all-latest-gpu/Dockerfile` | 370 | 2,945 |
| `transformers/docker/transformers-cpu/Dockerfile` | 72 | 629 |
| `transformers/docker/transformers-doc-builder/Dockerfile` | 126 | 1,253 |
| `transformers/docker/transformers-gpu/Dockerfile` | 93 | 846 |
| `transformers/docker/transformers-pytorch-cpu/Dockerfile` | 70 | 608 |
| `transformers/docker/transformers-pytorch-deepspeed-latest-gpu/Dockerfile` | 205 | 1,611 |
| `transformers/docker/transformers-pytorch-deepspeed-nightly-gpu/Dockerfile` | 228 | 1,800 |
| `transformers/docker/transformers-pytorch-gpu/Dockerfile` | 197 | 1,828 |
| `transformers/docker/transformers-pytorch-tpu/Dockerfile` | 263 | 2,877 |
| `transformers/docker/transformers-pytorch-tpu/bert-base-cased.jsonnet` | 84 | 937 |
| `transformers/docker/transformers-pytorch-tpu/dataset.yaml` | 72 | 797 |
| `transformers/docker/transformers-pytorch-tpu/docker-entrypoint.sh` | 19 | 247 |
| `transformers/docker/transformers-tensorflow-cpu/Dockerfile` | 70 | 613 |
| `transformers/docker/transformers-tensorflow-gpu/Dockerfile` | 129 | 995 |
| `transformers/docs/README.md` | 2,572 | 17,848 |
| `transformers/docs/TRANSLATING.md` | 465 | 3,389 |
| `transformers/docs/source/_config.py` | 54 | 518 |
| `transformers/docs/source/en/_config.py` | 54 | 518 |
| `transformers/docs/source/en/_toctree.yml` | 1,286 | 12,665 |
| `transformers/docs/source/en/accelerate.mdx` | 577 | 4,894 |
| `transformers/docs/source/en/add_new_model.mdx` | 7,505 | 50,447 |
| `transformers/docs/source/en/add_new_pipeline.mdx` | 918 | 6,566 |
| `transformers/docs/source/en/autoclass_tutorial.mdx` | 727 | 5,544 |
| `transformers/docs/source/en/benchmarks.mdx` | 1,677 | 17,753 |
| `transformers/docs/source/en/bertology.mdx` | 273 | 2,009 |
| `transformers/docs/source/en/big_models.mdx` | 868 | 6,330 |
| `transformers/docs/source/en/community.mdx` | 1,492 | 26,026 |
| `transformers/docs/source/en/converting_tensorflow_models.mdx` | 682 | 6,740 |
| `transformers/docs/source/en/create_a_model.mdx` | 1,840 | 15,264 |
| `transformers/docs/source/en/custom_models.mdx` | 1,940 | 14,779 |
| `transformers/docs/source/en/debugging.mdx` | 1,686 | 13,126 |
| `transformers/docs/source/en/fast_tokenizers.mdx` | 362 | 2,735 |
| `transformers/docs/source/en/glossary.mdx` | 2,047 | 13,743 |
| `transformers/docs/source/en/index.mdx` | 6,124 | 55,251 |
| `transformers/docs/source/en/installation.mdx` | 1,131 | 9,389 |
| `transformers/docs/source/en/internal/file_utils.mdx` | 155 | 1,276 |
| `transformers/docs/source/en/internal/generation_utils.mdx` | 694 | 6,950 |
| `transformers/docs/source/en/internal/modeling_utils.mdx` | 211 | 2,218 |
| `transformers/docs/source/en/internal/pipelines_utils.mdx` | 145 | 1,213 |
| `transformers/docs/source/en/internal/tokenization_utils.mdx` | 159 | 1,376 |
| `transformers/docs/source/en/internal/trainer_utils.mdx` | 151 | 1,218 |
| `transformers/docs/source/en/main_classes/callback.mdx` | 454 | 3,883 |
| `transformers/docs/source/en/main_classes/configuration.mdx` | 157 | 1,167 |
| `transformers/docs/source/en/main_classes/data_collator.mdx` | 219 | 2,076 |
| `transformers/docs/source/en/main_classes/deepspeed.mdx` | 10,070 | 78,834 |
| `transformers/docs/source/en/main_classes/feature_extractor.mdx` | 161 | 1,307 |
| `transformers/docs/source/en/main_classes/keras_callbacks.mdx` | 115 | 842 |
| `transformers/docs/source/en/main_classes/logging.mdx` | 418 | 3,453 |
| `transformers/docs/source/en/main_classes/model.mdx` | 826 | 6,321 |
| `transformers/docs/source/en/main_classes/onnx.mdx` | 210 | 1,679 |
| `transformers/docs/source/en/main_classes/optimizer_schedules.mdx` | 198 | 2,125 |
| `transformers/docs/source/en/main_classes/output.mdx` | 595 | 7,938 |
| `transformers/docs/source/en/main_classes/pipelines.mdx` | 1,601 | 14,356 |
| `transformers/docs/source/en/main_classes/processors.mdx` | 706 | 6,543 |
| `transformers/docs/source/en/main_classes/text_generation.mdx` | 156 | 1,466 |
| `transformers/docs/source/en/main_classes/tokenizer.mdx` | 513 | 3,892 |
| `transformers/docs/source/en/main_classes/trainer.mdx` | 3,728 | 28,208 |
| `transformers/docs/source/en/migration.mdx` | 1,921 | 14,895 |
| `transformers/docs/source/en/model_doc/albert.mdx` | 522 | 4,795 |
| `transformers/docs/source/en/model_doc/auto.mdx` | 542 | 6,143 |
| `transformers/docs/source/en/model_doc/bart.mdx` | 604 | 5,424 |
| `transformers/docs/source/en/model_doc/barthez.mdx` | 355 | 2,638 |
| `transformers/docs/source/en/model_doc/bartpho.mdx` | 444 | 3,750 |
| `transformers/docs/source/en/model_doc/beit.mdx` | 720 | 5,977 |
| `transformers/docs/source/en/model_doc/bert-generation.mdx` | 510 | 4,402 |
| `transformers/docs/source/en/model_doc/bert-japanese.mdx` | 292 | 2,505 |
| `transformers/docs/source/en/model_doc/bert.mdx` | 561 | 5,225 |
| `transformers/docs/source/en/model_doc/bertweet.mdx` | 306 | 2,437 |
| `transformers/docs/source/en/model_doc/big_bird.mdx` | 620 | 5,181 |
| `transformers/docs/source/en/model_doc/bigbird_pegasus.mdx` | 533 | 4,090 |
| `transformers/docs/source/en/model_doc/blenderbot-small.mdx` | 414 | 3,589 |
| `transformers/docs/source/en/model_doc/blenderbot.mdx` | 530 | 4,548 |
| `transformers/docs/source/en/model_doc/bloom.mdx` | 222 | 1,972 |
| `transformers/docs/source/en/model_doc/bort.mdx` | 400 | 2,766 |
| `transformers/docs/source/en/model_doc/byt5.mdx` | 1,058 | 7,229 |
| `transformers/docs/source/en/model_doc/camembert.mdx` | 393 | 3,512 |
| `transformers/docs/source/en/model_doc/canine.mdx` | 749 | 5,858 |
| `transformers/docs/source/en/model_doc/clip.mdx` | 789 | 6,035 |
| `transformers/docs/source/en/model_doc/codegen.mdx` | 529 | 4,215 |
| `transformers/docs/source/en/model_doc/convbert.mdx` | 420 | 3,629 |
| `transformers/docs/source/en/model_doc/convnext.mdx` | 431 | 3,549 |
| `transformers/docs/source/en/model_doc/cpm.mdx` | 348 | 2,447 |
| `transformers/docs/source/en/model_doc/ctrl.mdx` | 479 | 3,611 |
| `transformers/docs/source/en/model_doc/cvt.mdx` | 469 | 3,664 |
| `transformers/docs/source/en/model_doc/data2vec.mdx` | 544 | 5,274 |
| `transformers/docs/source/en/model_doc/deberta-v2.mdx` | 645 | 5,477 |
| `transformers/docs/source/en/model_doc/deberta.mdx` | 457 | 3,891 |
| `transformers/docs/source/en/model_doc/decision_transformer.mdx` | 315 | 2,430 |
| `transformers/docs/source/en/model_doc/deit.mdx` | 785 | 5,822 |
| `transformers/docs/source/en/model_doc/detr.mdx` | 1,841 | 13,878 |
| `transformers/docs/source/en/model_doc/dialogpt.mdx` | 418 | 2,945 |
| `transformers/docs/source/en/model_doc/distilbert.mdx` | 535 | 4,901 |
| `transformers/docs/source/en/model_doc/dit.mdx` | 504 | 4,321 |
| `transformers/docs/source/en/model_doc/dpr.mdx` | 333 | 2,892 |
| `transformers/docs/source/en/model_doc/dpt.mdx` | 380 | 3,004 |
| `transformers/docs/source/en/model_doc/electra.mdx` | 757 | 6,267 |
| `transformers/docs/source/en/model_doc/encoder-decoder.mdx` | 900 | 7,556 |
| `transformers/docs/source/en/model_doc/flaubert.mdx` | 425 | 3,605 |
| `transformers/docs/source/en/model_doc/flava.mdx` | 354 | 2,897 |
| `transformers/docs/source/en/model_doc/fnet.mdx` | 483 | 3,756 |
| `transformers/docs/source/en/model_doc/fsmt.mdx` | 346 | 2,746 |
| `transformers/docs/source/en/model_doc/funnel.mdx` | 571 | 4,987 |
| `transformers/docs/source/en/model_doc/glpn.mdx` | 464 | 3,799 |
| `transformers/docs/source/en/model_doc/gpt2.mdx` | 539 | 4,458 |
| `transformers/docs/source/en/model_doc/gpt_neo.mdx` | 291 | 2,347 |
| `transformers/docs/source/en/model_doc/gpt_neox.mdx` | 373 | 2,988 |
| `transformers/docs/source/en/model_doc/gptj.mdx` | 703 | 5,645 |
| `transformers/docs/source/en/model_doc/herbert.mdx` | 408 | 3,265 |
| `transformers/docs/source/en/model_doc/hubert.mdx` | 411 | 3,011 |
| `transformers/docs/source/en/model_doc/ibert.mdx` | 383 | 2,976 |
| `transformers/docs/source/en/model_doc/imagegpt.mdx` | 793 | 5,592 |
| `transformers/docs/source/en/model_doc/layoutlm.mdx` | 655 | 5,352 |
| `transformers/docs/source/en/model_doc/layoutlmv2.mdx` | 2,062 | 16,001 |
| `transformers/docs/source/en/model_doc/layoutlmv3.mdx` | 507 | 4,409 |
| `transformers/docs/source/en/model_doc/layoutxlm.mdx` | 385 | 3,274 |
| `transformers/docs/source/en/model_doc/led.mdx` | 537 | 4,802 |
| `transformers/docs/source/en/model_doc/levit.mdx` | 747 | 5,948 |
| `transformers/docs/source/en/model_doc/longformer.mdx` | 721 | 6,904 |
| `transformers/docs/source/en/model_doc/longt5.mdx` | 732 | 5,893 |
| `transformers/docs/source/en/model_doc/luke.mdx` | 1,028 | 8,603 |
| `transformers/docs/source/en/model_doc/lxmert.mdx` | 582 | 4,762 |
| `transformers/docs/source/en/model_doc/m2m_100.mdx` | 656 | 5,425 |
| `transformers/docs/source/en/model_doc/marian.mdx` | 924 | 7,875 |
| `transformers/docs/source/en/model_doc/maskformer.mdx` | 566 | 4,906 |
| `transformers/docs/source/en/model_doc/mbart.mdx` | 999 | 9,131 |
| `transformers/docs/source/en/model_doc/mctct.mdx` | 356 | 2,719 |
| `transformers/docs/source/en/model_doc/megatron-bert.mdx` | 627 | 5,437 |
| `transformers/docs/source/en/model_doc/megatron_gpt2.mdx` | 548 | 4,167 |
| `transformers/docs/source/en/model_doc/mluke.mdx` | 397 | 3,030 |
| `transformers/docs/source/en/model_doc/mobilebert.mdx` | 540 | 4,749 |
| `transformers/docs/source/en/model_doc/mpnet.mdx` | 456 | 3,742 |
| `transformers/docs/source/en/model_doc/mt5.mdx` | 379 | 3,258 |
| `transformers/docs/source/en/model_doc/nezha.mdx` | 324 | 2,743 |
| `transformers/docs/source/en/model_doc/nystromformer.mdx` | 365 | 2,957 |
| `transformers/docs/source/en/model_doc/openai-gpt.mdx` | 537 | 4,420 |
| `transformers/docs/source/en/model_doc/opt.mdx` | 359 | 2,679 |
| `transformers/docs/source/en/model_doc/pegasus.mdx` | 602 | 5,452 |
| `transformers/docs/source/en/model_doc/perceiver.mdx` | 1,102 | 9,712 |
| `transformers/docs/source/en/model_doc/phobert.mdx` | 265 | 2,185 |
| `transformers/docs/source/en/model_doc/plbart.mdx` | 630 | 5,533 |
| `transformers/docs/source/en/model_doc/poolformer.mdx` | 600 | 4,493 |
| `transformers/docs/source/en/model_doc/prophetnet.mdx` | 365 | 3,212 |
| `transformers/docs/source/en/model_doc/qdqbert.mdx` | 715 | 6,154 |
| `transformers/docs/source/en/model_doc/rag.mdx` | 479 | 3,818 |
| `transformers/docs/source/en/model_doc/realm.mdx` | 403 | 3,235 |
| `transformers/docs/source/en/model_doc/reformer.mdx` | 1,190 | 9,023 |
| `transformers/docs/source/en/model_doc/regnet.mdx` | 406 | 2,945 |
| `transformers/docs/source/en/model_doc/rembert.mdx` | 463 | 4,008 |
| `transformers/docs/source/en/model_doc/resnet.mdx` | 441 | 3,305 |
| `transformers/docs/source/en/model_doc/retribert.mdx` | 173 | 1,390 |
| `transformers/docs/source/en/model_doc/roberta.mdx` | 540 | 4,807 |
| `transformers/docs/source/en/model_doc/roformer.mdx` | 444 | 4,305 |
| `transformers/docs/source/en/model_doc/segformer.mdx` | 945 | 7,178 |
| `transformers/docs/source/en/model_doc/sew-d.mdx` | 310 | 2,296 |
| `transformers/docs/source/en/model_doc/sew.mdx` | 307 | 2,253 |
| `transformers/docs/source/en/model_doc/speech-encoder-decoder.mdx` | 198 | 1,694 |
| `transformers/docs/source/en/model_doc/speech_to_text.mdx` | 622 | 6,090 |
| `transformers/docs/source/en/model_doc/speech_to_text_2.mdx` | 460 | 4,508 |
| `transformers/docs/source/en/model_doc/splinter.mdx` | 529 | 3,971 |
| `transformers/docs/source/en/model_doc/squeezebert.mdx` | 505 | 3,966 |
| `transformers/docs/source/en/model_doc/swin.mdx` | 484 | 3,890 |
| `transformers/docs/source/en/model_doc/t5.mdx` | 2,105 | 17,099 |
| `transformers/docs/source/en/model_doc/t5v1.1.mdx` | 328 | 2,845 |
| `transformers/docs/source/en/model_doc/tapas.mdx` | 4,245 | 36,822 |
| `transformers/docs/source/en/model_doc/tapex.mdx` | 944 | 6,951 |
| `transformers/docs/source/en/model_doc/trajectory_transformer.mdx` | 370 | 2,700 |
| `transformers/docs/source/en/model_doc/transfo-xl.mdx` | 463 | 3,940 |
| `transformers/docs/source/en/model_doc/trocr.mdx` | 552 | 5,050 |
| `transformers/docs/source/en/model_doc/ul2.mdx` | 422 | 3,154 |
| `transformers/docs/source/en/model_doc/unispeech-sat.mdx` | 445 | 3,703 |
| `transformers/docs/source/en/model_doc/unispeech.mdx` | 360 | 2,910 |
| `transformers/docs/source/en/model_doc/van.mdx` | 371 | 2,951 |
| `transformers/docs/source/en/model_doc/vilt.mdx` | 520 | 4,041 |
| `transformers/docs/source/en/model_doc/vision-encoder-decoder.mdx` | 213 | 1,872 |
| `transformers/docs/source/en/model_doc/vision-text-dual-encoder.mdx` | 255 | 2,003 |
| `transformers/docs/source/en/model_doc/visual_bert.mdx` | 732 | 5,868 |
| `transformers/docs/source/en/model_doc/vit.mdx` | 928 | 7,348 |
| `transformers/docs/source/en/model_doc/vit_mae.mdx` | 611 | 4,785 |
| `transformers/docs/source/en/model_doc/wav2vec2-conformer.mdx` | 291 | 2,788 |
| `transformers/docs/source/en/model_doc/wav2vec2.mdx` | 444 | 3,991 |
| `transformers/docs/source/en/model_doc/wav2vec2_phoneme.mdx` | 380 | 2,860 |
| `transformers/docs/source/en/model_doc/wavlm.mdx` | 422 | 3,292 |
| `transformers/docs/source/en/model_doc/xglm.mdx` | 454 | 3,396 |
| `transformers/docs/source/en/model_doc/xlm-prophetnet.mdx` | 360 | 2,968 |
| `transformers/docs/source/en/model_doc/xlm-roberta-xl.mdx` | 331 | 2,786 |
| `transformers/docs/source/en/model_doc/xlm-roberta.mdx` | 553 | 4,957 |
| `transformers/docs/source/en/model_doc/xlm.mdx` | 478 | 3,981 |
| `transformers/docs/source/en/model_doc/xlnet.mdx` | 524 | 5,225 |
| `transformers/docs/source/en/model_doc/xls_r.mdx` | 390 | 2,729 |
| `transformers/docs/source/en/model_doc/xlsr_wav2vec2.mdx` | 346 | 2,528 |
| `transformers/docs/source/en/model_doc/yolos.mdx` | 398 | 3,121 |
| `transformers/docs/source/en/model_doc/yoso.mdx` | 539 | 4,143 |
| `transformers/docs/source/en/model_sharing.mdx` | 1,308 | 10,096 |
| `transformers/docs/source/en/model_summary.mdx` | 5,356 | 46,112 |
| `transformers/docs/source/en/multilingual.mdx` | 990 | 8,071 |
| `transformers/docs/source/en/pad_truncation.mdx` | 785 | 7,264 |
| `transformers/docs/source/en/perf_hardware.mdx` | 1,129 | 7,401 |
| `transformers/docs/source/en/perf_infer_cpu.mdx` | 401 | 3,220 |
| `transformers/docs/source/en/perf_infer_gpu_many.mdx` | 123 | 794 |
| `transformers/docs/source/en/perf_infer_gpu_one.mdx` | 123 | 788 |
| `transformers/docs/source/en/perf_infer_special.mdx` | 111 | 729 |
| `transformers/docs/source/en/perf_train_cpu.mdx` | 412 | 3,180 |
| `transformers/docs/source/en/perf_train_gpu_many.mdx` | 4,974 | 33,731 |
| `transformers/docs/source/en/perf_train_gpu_one.mdx` | 5,659 | 41,532 |
| `transformers/docs/source/en/perf_train_special.mdx` | 145 | 972 |
| `transformers/docs/source/en/perf_train_tpu.mdx` | 143 | 940 |
| `transformers/docs/source/en/performance.mdx` | 635 | 4,161 |
| `transformers/docs/source/en/perplexity.mdx` | 1,076 | 7,665 |
| `transformers/docs/source/en/philosophy.mdx` | 701 | 4,934 |
| `transformers/docs/source/en/pipeline_tutorial.mdx` | 892 | 6,500 |
| `transformers/docs/source/en/pr_checks.mdx` | 1,063 | 6,374 |
| `transformers/docs/source/en/preprocessing.mdx` | 3,010 | 22,599 |
| `transformers/docs/source/en/quicktour.mdx` | 2,116 | 16,086 |
| `transformers/docs/source/en/run_scripts.mdx` | 1,623 | 16,577 |
| `transformers/docs/source/en/sagemaker.mdx` | 143 | 1,131 |
| `transformers/docs/source/en/serialization.mdx` | 3,367 | 26,617 |
| `transformers/docs/source/en/task_summary.mdx` | 7,033 | 54,963 |
| `transformers/docs/source/en/tasks/asr.mdx` | 1,024 | 9,554 |
| `transformers/docs/source/en/tasks/audio_classification.mdx` | 842 | 7,439 |
| `transformers/docs/source/en/tasks/image_classification.mdx` | 769 | 6,403 |
| `transformers/docs/source/en/tasks/language_modeling.mdx` | 1,970 | 16,547 |
| `transformers/docs/source/en/tasks/multiple_choice.mdx` | 1,232 | 10,906 |
| `transformers/docs/source/en/tasks/question_answering.mdx` | 1,177 | 10,253 |
| `transformers/docs/source/en/tasks/sequence_classification.mdx` | 1,050 | 8,686 |
| `transformers/docs/source/en/tasks/summarization.mdx` | 1,988 | 14,959 |
| `transformers/docs/source/en/tasks/token_classification.mdx` | 1,152 | 10,139 |
| `transformers/docs/source/en/tasks/translation.mdx` | 870 | 7,709 |
| `transformers/docs/source/en/testing.mdx` | 5,579 | 39,692 |
| `transformers/docs/source/en/tokenizer_summary.mdx` | 2,623 | 17,526 |
| `transformers/docs/source/en/training.mdx` | 1,842 | 14,984 |
| `transformers/docs/source/en/troubleshooting.mdx` | 1,025 | 7,662 |
| `transformers/docs/source/es/_config.py` | 54 | 514 |
| `transformers/docs/source/es/_toctree.yml` | 148 | 1,291 |
| `transformers/docs/source/es/accelerate.mdx` | 577 | 5,148 |
| `transformers/docs/source/es/autoclass_tutorial.mdx` | 744 | 6,015 |
| `transformers/docs/source/es/bertology.mdx` | 288 | 2,138 |
| `transformers/docs/source/es/create_a_model.mdx` | 2,066 | 17,255 |
| `transformers/docs/source/es/fast_tokenizers.mdx` | 367 | 2,963 |
| `transformers/docs/source/es/index.mdx` | 5,378 | 48,270 |
| `transformers/docs/source/es/installation.mdx` | 1,195 | 10,147 |
| `transformers/docs/source/es/model_sharing.mdx` | 1,387 | 11,218 |
| `transformers/docs/source/es/multilingual.mdx` | 1,029 | 8,423 |
| `transformers/docs/source/es/philosophy.mdx` | 732 | 5,498 |
| `transformers/docs/source/es/pipeline_tutorial.mdx` | 841 | 6,454 |
| `transformers/docs/source/es/preprocessing.mdx` | 3,607 | 29,746 |
| `transformers/docs/source/es/quicktour.mdx` | 2,210 | 17,583 |
| `transformers/docs/source/es/sagemaker.mdx` | 142 | 1,150 |
| `transformers/docs/source/es/tasks/image_classification.mdx` | 827 | 6,778 |
| `transformers/docs/source/es/tasks/language_modeling.mdx` | 2,054 | 17,567 |
| `transformers/docs/source/es/training.mdx` | 1,910 | 15,741 |
| `transformers/docs/source/it/_config.py` | 58 | 555 |
| `transformers/docs/source/it/_toctree.yml` | 41 | 352 |
| `transformers/docs/source/it/autoclass_tutorial.mdx` | 720 | 5,898 |
| `transformers/docs/source/it/index.mdx` | 5,775 | 51,771 |
| `transformers/docs/source/it/installation.mdx` | 1,149 | 9,908 |
| `transformers/docs/source/it/pipeline_tutorial.mdx` | 893 | 6,807 |
| `transformers/docs/source/it/quicktour.mdx` | 2,190 | 17,929 |
| `transformers/docs/source/pt/_config.py` | 54 | 518 |
| `transformers/docs/source/pt/_toctree.yml` | 94 | 831 |
| `transformers/docs/source/pt/accelerate.mdx` | 574 | 5,075 |
| `transformers/docs/source/pt/fast_tokenizers.mdx` | 348 | 2,822 |
| `transformers/docs/source/pt/index.mdx` | 5,456 | 49,233 |
| `transformers/docs/source/pt/installation.mdx` | 1,204 | 10,187 |
| `transformers/docs/source/pt/multilingual.mdx` | 1,049 | 8,532 |
| `transformers/docs/source/pt/pipeline_tutorial.mdx` | 855 | 6,596 |
| `transformers/docs/source/pt/quicktour.mdx` | 2,126 | 16,756 |
| `transformers/docs/source/pt/tasks/sequence_classification.mdx` | 1,128 | 9,337 |
| `transformers/docs/source/pt/tasks/token_classification.mdx` | 1,233 | 10,824 |
| `transformers/docs/source/pt/training.mdx` | 1,989 | 16,323 |
| `transformers/examples/README.md` | 467 | 5,694 |
| `transformers/examples/flax/README.md` | 829 | 6,546 |
| `transformers/examples/flax/_tests_requirements.txt` | 9 | 68 |
| `transformers/examples/flax/conftest.py` | 210 | 1,714 |
| `transformers/examples/flax/image-captioning/README.md` | 321 | 3,273 |
| `transformers/examples/flax/image-captioning/create_model_from_encoder_decoder_models.py` | 411 | 4,526 |
| `transformers/examples/flax/image-captioning/run_image_captioning_flax.py` | 4,819 | 54,167 |
| `transformers/examples/flax/language-modeling/README.md` | 1,755 | 16,265 |
| `transformers/examples/flax/language-modeling/requirements.txt` | 7 | 69 |
| `transformers/examples/flax/language-modeling/run_clm_flax.py` | 3,298 | 35,720 |
| `transformers/examples/flax/language-modeling/run_mlm_flax.py` | 3,456 | 37,555 |
| `transformers/examples/flax/language-modeling/run_t5_mlm_flax.py` | 3,941 | 42,934 |
| `transformers/examples/flax/language-modeling/t5_tokenizer_model.py` | 258 | 3,882 |
| `transformers/examples/flax/question-answering/README.md` | 459 | 3,324 |
| `transformers/examples/flax/question-answering/requirements.txt` | 7 | 69 |
| `transformers/examples/flax/question-answering/run_qa.py` | 4,621 | 48,527 |
| `transformers/examples/flax/question-answering/utils_qa.py` | 2,297 | 22,777 |
| `transformers/examples/flax/summarization/README.md` | 219 | 1,754 |
| `transformers/examples/flax/summarization/requirements.txt` | 7 | 69 |
| `transformers/examples/flax/summarization/run_summarization_flax.py` | 3,716 | 40,870 |
| `transformers/examples/flax/test_flax_examples.py` | 532 | 8,481 |
| `transformers/examples/flax/text-classification/README.md` | 893 | 6,620 |
| `transformers/examples/flax/text-classification/requirements.txt` | 7 | 69 |
| `transformers/examples/flax/text-classification/run_flax_glue.py` | 2,604 | 27,481 |
| `transformers/examples/flax/token-classification/README.md` | 270 | 1,921 |
| `transformers/examples/flax/token-classification/requirements.txt` | 8 | 76 |
| `transformers/examples/flax/token-classification/run_flax_ner.py` | 3,274 | 35,026 |
| `transformers/examples/flax/vision/README.md` | 304 | 2,501 |
| `transformers/examples/flax/vision/requirements.txt` | 10 | 200 |
| `transformers/examples/flax/vision/run_image_classification.py` | 2,026 | 22,341 |
| `transformers/examples/legacy/README.md` | 129 | 871 |
| `transformers/examples/legacy/multiple_choice/run_multiple_choice.py` | 753 | 8,297 |
| `transformers/examples/legacy/multiple_choice/utils_multiple_choice.py` | 1,724 | 20,884 |
| `transformers/examples/legacy/pytorch-lightning/lightning_base.py` | 1,058 | 15,050 |
| `transformers/examples/legacy/pytorch-lightning/requirements.txt` | 25 | 231 |
| `transformers/examples/legacy/pytorch-lightning/run_glue.py` | 662 | 8,050 |
| `transformers/examples/legacy/pytorch-lightning/run_glue.sh` | 93 | 907 |
| `transformers/examples/legacy/pytorch-lightning/run_ner.py` | 760 | 9,726 |
| `transformers/examples/legacy/pytorch-lightning/run_ner.sh` | 196 | 1,703 |
| `transformers/examples/legacy/pytorch-lightning/run_pos.sh` | 111 | 1,112 |
| `transformers/examples/legacy/question-answering/README.md` | 484 | 4,781 |
| `transformers/examples/legacy/question-answering/run_squad.py` | 2,981 | 34,918 |
| `transformers/examples/legacy/question-answering/run_squad_trainer.py` | 654 | 6,804 |
| `transformers/examples/legacy/run_camembert.py` | 133 | 1,935 |
| `transformers/examples/legacy/run_chinese_ref.py` | 597 | 5,274 |
| `transformers/examples/legacy/run_language_modeling.py` | 1,291 | 13,897 |
| `transformers/examples/legacy/run_openai_gpt.py` | 1,218 | 14,289 |
| `transformers/examples/legacy/run_swag.py` | 2,708 | 30,219 |
| `transformers/examples/legacy/run_transfo_xl.py` | 605 | 6,205 |
| `transformers/examples/legacy/seq2seq/README.md` | 1,949 | 15,101 |
| `transformers/examples/legacy/seq2seq/__init__.py` | 6 | 87 |
| `transformers/examples/legacy/seq2seq/convert_model_to_fp16.py` | 188 | 1,383 |
| `transformers/examples/legacy/seq2seq/download_wmt.py` | 311 | 2,634 |
| `transformers/examples/legacy/seq2seq/finetune.sh` | 146 | 979 |
| `transformers/examples/legacy/seq2seq/finetune_tpu.sh` | 149 | 1,026 |
| `transformers/examples/legacy/seq2seq/finetune_trainer.py` | 1,183 | 13,961 |
| `transformers/examples/legacy/seq2seq/minify_dataset.py` | 154 | 1,160 |
| `transformers/examples/legacy/seq2seq/old_test_calculate_rouge.py` | 730 | 5,762 |
| `transformers/examples/legacy/seq2seq/old_test_datasets.py` | 873 | 11,060 |
| `transformers/examples/legacy/seq2seq/old_test_fsmt_bleu_score.py` | 246 | 2,504 |
| `transformers/examples/legacy/seq2seq/old_test_seq2seq_examples.py` | 457 | 4,987 |
| `transformers/examples/legacy/seq2seq/old_test_seq2seq_examples_multi_gpu.py` | 220 | 2,032 |
| `transformers/examples/legacy/seq2seq/old_test_tatoeba_conversion.py` | 150 | 1,383 |
| `transformers/examples/legacy/seq2seq/pack_dataset.py` | 348 | 3,385 |
| `transformers/examples/legacy/seq2seq/requirements.txt` | 24 | 227 |
| `transformers/examples/legacy/seq2seq/romanian_postprocessing.md` | 183 | 1,871 |
| `transformers/examples/legacy/seq2seq/rouge_cli.py` | 156 | 1,180 |
| `transformers/examples/legacy/seq2seq/run_distributed_eval.py` | 882 | 10,216 |
| `transformers/examples/legacy/seq2seq/run_eval.py` | 698 | 7,324 |
| `transformers/examples/legacy/seq2seq/run_eval_search.py` | 705 | 6,011 |
| `transformers/examples/legacy/seq2seq/save_len_file.py` | 215 | 2,111 |
| `transformers/examples/legacy/seq2seq/save_randomly_initialized_model.py` | 169 | 1,539 |
| `transformers/examples/legacy/seq2seq/sentence_splitter.py` | 169 | 1,239 |
| `transformers/examples/legacy/seq2seq/seq2seq_trainer.py` | 916 | 11,214 |
| `transformers/examples/legacy/seq2seq/seq2seq_training_args.py` | 300 | 2,678 |
| `transformers/examples/legacy/seq2seq/test_data/fsmt/build-eval-data.py` | 90 | 877 |
| `transformers/examples/legacy/seq2seq/test_data/fsmt/fsmt_val_data.json` | 1,035 | 9,073 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/test.source` | 2,032 | 12,053 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/test.target` | 2,201 | 14,518 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/train.len` | — | 26 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/train.source` | 682 | 4,678 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/train.target` | 751 | 6,111 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/val.len` | — | 40 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/val.source` | 1,664 | 9,589 |
| `transformers/examples/legacy/seq2seq/test_data/wmt_en_ro/val.target` | 1,810 | 11,443 |
| `transformers/examples/legacy/seq2seq/train_distil_marian_enro.sh` | 173 | 1,534 |
| `transformers/examples/legacy/seq2seq/train_distil_marian_enro_tpu.sh` | 174 | 1,529 |
| `transformers/examples/legacy/seq2seq/train_distilbart_cnn.sh` | 169 | 1,500 |
| `transformers/examples/legacy/seq2seq/train_mbart_cc25_enro.sh` | 168 | 1,407 |
| `transformers/examples/legacy/seq2seq/utils.py` | 2,230 | 25,288 |
| `transformers/examples/legacy/seq2seq/xla_spawn.py` | 281 | 2,489 |
| `transformers/examples/legacy/text-classification/run_tf_text_classification.py` | 976 | 10,735 |
| `transformers/examples/legacy/token-classification/README.md` | 1,369 | 11,281 |
| `transformers/examples/legacy/token-classification/run.sh` | 174 | 1,482 |
| `transformers/examples/legacy/token-classification/run_chunk.sh` | 103 | 1,024 |
| `transformers/examples/legacy/token-classification/run_ner.py` | 1,057 | 12,270 |
| `transformers/examples/legacy/token-classification/run_pos.sh` | 100 | 1,022 |
| `transformers/examples/legacy/token-classification/run_tf_ner.py` | 946 | 11,238 |
| `transformers/examples/legacy/token-classification/scripts/preprocess.py` | 88 | 993 |
| `transformers/examples/legacy/token-classification/tasks.py` | 432 | 5,509 |
| `transformers/examples/legacy/token-classification/utils_ner.py` | 1,373 | 15,647 |
| `transformers/examples/pytorch/README.md` | 1,554 | 14,309 |
| `transformers/examples/pytorch/_tests_requirements.txt` | 30 | 330 |
| `transformers/examples/pytorch/audio-classification/README.md` | 633 | 6,117 |
| `transformers/examples/pytorch/audio-classification/requirements.txt` | 4 | 46 |
| `transformers/examples/pytorch/audio-classification/run_audio_classification.py` | 1,532 | 16,934 |
| `transformers/examples/pytorch/benchmarking/README.md` | 175 | 1,654 |
| `transformers/examples/pytorch/benchmarking/plot_csv_file.py` | 564 | 6,407 |
| `transformers/examples/pytorch/benchmarking/requirements.txt` | 3 | 12 |
| `transformers/examples/pytorch/benchmarking/run_benchmark.py` | 208 | 1,836 |
| `transformers/examples/pytorch/conftest.py` | 210 | 1,714 |
| `transformers/examples/pytorch/contrastive-image-text/README.md` | 444 | 3,972 |
| `transformers/examples/pytorch/contrastive-image-text/requirements.txt` | 3 | 47 |
| `transformers/examples/pytorch/contrastive-image-text/run_clip.py` | 2,065 | 22,664 |
| `transformers/examples/pytorch/image-classification/README.md` | 1,046 | 9,001 |
| `transformers/examples/pytorch/image-classification/requirements.txt` | 3 | 49 |
| `transformers/examples/pytorch/image-classification/run_image_classification.py` | 1,343 | 15,141 |
| `transformers/examples/pytorch/image-classification/run_image_classification_no_trainer.py` | 2,026 | 24,360 |
| `transformers/examples/pytorch/image-pretraining/README.md` | 1,253 | 10,416 |
| `transformers/examples/pytorch/image-pretraining/requirements.txt` | 3 | 47 |
| `transformers/examples/pytorch/image-pretraining/run_mae.py` | 1,356 | 15,246 |
| `transformers/examples/pytorch/image-pretraining/run_mim.py` | 1,668 | 18,674 |
| `transformers/examples/pytorch/language-modeling/README.md` | 971 | 7,449 |
| `transformers/examples/pytorch/language-modeling/requirements.txt` | 11 | 75 |
| `transformers/examples/pytorch/language-modeling/run_clm.py` | 2,285 | 25,025 |
| `transformers/examples/pytorch/language-modeling/run_clm_no_trainer.py` | 2,495 | 27,864 |
| `transformers/examples/pytorch/language-modeling/run_mlm.py` | 2,371 | 26,607 |
| `transformers/examples/pytorch/language-modeling/run_mlm_no_trainer.py` | 2,671 | 30,156 |
| `transformers/examples/pytorch/language-modeling/run_plm.py` | 2,120 | 23,660 |
| `transformers/examples/pytorch/multiple-choice/README.md` | 502 | 3,702 |
| `transformers/examples/pytorch/multiple-choice/requirements.txt` | 8 | 57 |
| `transformers/examples/pytorch/multiple-choice/run_no_trainer.sh` | 113 | 782 |
| `transformers/examples/pytorch/multiple-choice/run_swag.py` | 1,858 | 19,705 |
| `transformers/examples/pytorch/multiple-choice/run_swag_no_trainer.py` | 2,561 | 27,792 |
| `transformers/examples/pytorch/question-answering/README.md` | 850 | 7,174 |
| `transformers/examples/pytorch/question-answering/requirements.txt` | 7 | 44 |
| `transformers/examples/pytorch/question-answering/run_qa.py` | 2,947 | 31,492 |
| `transformers/examples/pytorch/question-answering/run_qa_beam_search.py` | 3,049 | 33,060 |
| `transformers/examples/pytorch/question-answering/run_qa_beam_search_no_trainer.py` | 4,120 | 46,506 |
| `transformers/examples/pytorch/question-answering/run_qa_no_trainer.py` | 4,077 | 44,481 |
| `transformers/examples/pytorch/question-answering/run_seq2seq_qa.py` | 2,877 | 31,396 |
| `transformers/examples/pytorch/question-answering/trainer_qa.py` | 419 | 4,741 |
| `transformers/examples/pytorch/question-answering/trainer_seq2seq_qa.py` | 487 | 5,555 |
| `transformers/examples/pytorch/question-answering/utils_qa.py` | 2,297 | 22,777 |
| `transformers/examples/pytorch/semantic-segmentation/README.md` | 1,104 | 10,372 |
| `transformers/examples/pytorch/semantic-segmentation/requirements.txt` | 7 | 74 |
| `transformers/examples/pytorch/semantic-segmentation/run_semantic_segmentation.py` | 1,732 | 19,456 |
| `transformers/examples/pytorch/semantic-segmentation/run_semantic_segmentation_no_trainer.py` | 2,212 | 27,163 |
| `transformers/examples/pytorch/speech-pretraining/README.md` | 630 | 6,713 |
| `transformers/examples/pytorch/speech-pretraining/requirements.txt` | 11 | 71 |
| `transformers/examples/pytorch/speech-pretraining/run_wav2vec2_pretraining_no_trainer.py` | 2,434 | 29,817 |
| `transformers/examples/pytorch/speech-recognition/README.md` | 2,295 | 28,102 |
| `transformers/examples/pytorch/speech-recognition/requirements.txt` | 9 | 57 |
| `transformers/examples/pytorch/speech-recognition/run_speech_recognition_ctc.py` | 2,905 | 31,336 |
| `transformers/examples/pytorch/speech-recognition/run_speech_recognition_seq2seq.py` | 1,899 | 21,534 |
| `transformers/examples/pytorch/summarization/README.md` | 1,169 | 8,549 |
| `transformers/examples/pytorch/summarization/requirements.txt` | 14 | 98 |
| `transformers/examples/pytorch/summarization/run_summarization.py` | 2,786 | 31,353 |
| `transformers/examples/pytorch/summarization/run_summarization_no_trainer.py` | 2,845 | 32,072 |
| `transformers/examples/pytorch/test_accelerate_examples.py` | 727 | 13,090 |
| `transformers/examples/pytorch/test_pytorch_examples.py` | 1,127 | 20,168 |
| `transformers/examples/pytorch/test_xla_examples.py` | 241 | 2,840 |
| `transformers/examples/pytorch/text-classification/README.md` | 1,128 | 8,660 |
| `transformers/examples/pytorch/text-classification/requirements.txt` | 13 | 94 |
| `transformers/examples/pytorch/text-classification/run_glue.py` | 2,532 | 26,981 |
| `transformers/examples/pytorch/text-classification/run_glue_no_trainer.py` | 2,538 | 27,896 |
| `transformers/examples/pytorch/text-classification/run_xnli.py` | 1,473 | 17,248 |
| `transformers/examples/pytorch/text-generation/README.md` | 145 | 1,173 |
| `transformers/examples/pytorch/text-generation/requirements.txt` | 7 | 46 |
| `transformers/examples/pytorch/text-generation/run_generation.py` | 1,061 | 10,991 |
| `transformers/examples/pytorch/token-classification/README.md` | 641 | 4,697 |
| `transformers/examples/pytorch/token-classification/requirements.txt` | 8 | 50 |
| `transformers/examples/pytorch/token-classification/run.sh` | 114 | 758 |
| `transformers/examples/pytorch/token-classification/run_ner.py` | 2,427 | 26,552 |
| `transformers/examples/pytorch/token-classification/run_ner_no_trainer.py` | 2,965 | 32,889 |
| `transformers/examples/pytorch/token-classification/run_no_trainer.sh` | 118 | 828 |
| `transformers/examples/pytorch/translation/README.md` | 932 | 8,071 |
| `transformers/examples/pytorch/translation/requirements.txt` | 15 | 101 |
| `transformers/examples/pytorch/translation/run_translation.py` | 2,530 | 28,254 |
| `transformers/examples/pytorch/translation/run_translation_no_trainer.py` | 2,800 | 31,271 |
| `transformers/examples/pytorch/xla_spawn.py` | 281 | 2,489 |
| `transformers/examples/research_projects/README.md` | 178 | 1,131 |
| `transformers/examples/research_projects/adversarial/README.md` | 156 | 1,425 |
| `transformers/examples/research_projects/adversarial/requirements.txt` | 3 | 22 |
| `transformers/examples/research_projects/adversarial/run_hans.py` | 764 | 8,264 |
| `transformers/examples/research_projects/adversarial/utils_hans.py` | 1,019 | 11,761 |
| `transformers/examples/research_projects/bert-loses-patience/README.md` | 439 | 3,354 |
| `transformers/examples/research_projects/bert-loses-patience/pabee/__init__.py` | 0 | 0 |
| `transformers/examples/research_projects/bert-loses-patience/pabee/modeling_pabee_albert.py` | 1,128 | 14,134 |
| `transformers/examples/research_projects/bert-loses-patience/pabee/modeling_pabee_bert.py` | 1,327 | 15,544 |
| `transformers/examples/research_projects/bert-loses-patience/requirements.txt` | 3 | 21 |
| `transformers/examples/research_projects/bert-loses-patience/run_glue_with_pabee.py` | 2,577 | 30,563 |
| `transformers/examples/research_projects/bert-loses-patience/test_run_glue_with_pabee.py` | 80 | 1,369 |
| `transformers/examples/research_projects/bertabs/README.md` | 409 | 2,896 |
| `transformers/examples/research_projects/bertabs/__init__.py` | 0 | 0 |
| `transformers/examples/research_projects/bertabs/configuration_bertabs.py` | 347 | 3,261 |
| `transformers/examples/research_projects/bertabs/convert_bertabs_original_pytorch_checkpoint.py` | 597 | 6,529 |
| `transformers/examples/research_projects/bertabs/modeling_bertabs.py` | 3,329 | 38,263 |
| `transformers/examples/research_projects/bertabs/requirements.txt` | 8 | 49 |
| `transformers/examples/research_projects/bertabs/run_summarization.py` | 906 | 10,203 |
| `transformers/examples/research_projects/bertabs/test_utils_summarization.py` | 505 | 4,419 |
| `transformers/examples/research_projects/bertabs/utils_summarization.py` | 619 | 5,753 |
| `transformers/examples/research_projects/bertology/requirements.txt` | 3 | 22 |
| `transformers/examples/research_projects/bertology/run_bertology.py` | 1,659 | 18,600 |
| `transformers/examples/research_projects/bertology/run_prune_gpt.py` | 1,351 | 15,497 |
| `transformers/examples/research_projects/codeparrot/README.md` | 1,391 | 10,377 |
| `transformers/examples/research_projects/codeparrot/requirements.txt` | 9 | 226 |
| `transformers/examples/research_projects/codeparrot/scripts/arguments.py` | 1,000 | 10,173 |
| `transformers/examples/research_projects/codeparrot/scripts/bpe_training.py` | 80 | 1,015 |
| `transformers/examples/research_projects/codeparrot/scripts/codeparrot_training.py` | 1,006 | 12,866 |
| `transformers/examples/research_projects/codeparrot/scripts/human_eval.py` | 817 | 9,006 |
| `transformers/examples/research_projects/codeparrot/scripts/initialize_model.py` | 80 | 892 |
| `transformers/examples/research_projects/codeparrot/scripts/minhash_deduplication.py` | 1,094 | 10,897 |
| `transformers/examples/research_projects/codeparrot/scripts/preprocessing.py` | 713 | 7,344 |
| `transformers/examples/research_projects/codeparrot/scripts/pretokenizing.py` | 97 | 1,271 |
| `transformers/examples/research_projects/codeparrot/scripts/tests/__init__.py` | 0 | 0 |
| `transformers/examples/research_projects/codeparrot/scripts/tests/test_deduplicate.py` | 74 | 1,005 |
| `transformers/examples/research_projects/codeparrot/scripts/validation_loss.py` | 276 | 3,496 |
| `transformers/examples/research_projects/decision_transformer/requirements.txt` | 241 | 4,217 |
| `transformers/examples/research_projects/decision_transformer/run_decision_transformer.py` | 417 | 5,570 |
| `transformers/examples/research_projects/deebert/README.md` | 251 | 1,897 |
| `transformers/examples/research_projects/deebert/entropy_eval.sh` | 84 | 904 |
| `transformers/examples/research_projects/deebert/eval_deebert.sh` | 69 | 790 |
| `transformers/examples/research_projects/deebert/requirements.txt` | 3 | 22 |
| `transformers/examples/research_projects/deebert/run_glue_deebert.py` | 2,612 | 31,749 |
| `transformers/examples/research_projects/deebert/src/__init__.py` | 0 | 0 |
| `transformers/examples/research_projects/deebert/src/modeling_highway_bert.py` | 1,471 | 17,668 |
| `transformers/examples/research_projects/deebert/src/modeling_highway_roberta.py` | 542 | 6,791 |
| `transformers/examples/research_projects/deebert/test_glue_deebert.py` | 207 | 3,690 |
| `transformers/examples/research_projects/deebert/train_deebert.sh` | 87 | 910 |
| `transformers/examples/research_projects/distillation/README.md` | 1,953 | 14,937 |
| `transformers/examples/research_projects/distillation/distiller.py` | 2,115 | 26,196 |
| `transformers/examples/research_projects/distillation/grouped_batch_sampler.py` | 490 | 4,349 |
| `transformers/examples/research_projects/distillation/lm_seqs_dataset.py` | 600 | 6,132 |
| `transformers/examples/research_projects/distillation/requirements.txt` | 6 | 96 |
| `transformers/examples/research_projects/distillation/run_squad_w_distillation.py` | 3,049 | 36,220 |
| `transformers/examples/research_projects/distillation/scripts/binarized_data.py` | 358 | 3,660 |
| `transformers/examples/research_projects/distillation/scripts/extract.py` | 364 | 4,489 |
| `transformers/examples/research_projects/distillation/scripts/extract_distilbert.py` | 294 | 4,355 |
| `transformers/examples/research_projects/distillation/scripts/token_counts.py` | 222 | 2,017 |
| `transformers/examples/research_projects/distillation/train.py` | 1,097 | 13,004 |
| `transformers/examples/research_projects/distillation/training_configs/distilbert-base-cased.json` | 26 | 277 |
| `transformers/examples/research_projects/distillation/training_configs/distilbert-base-multilingual-cased.json` | 26 | 278 |
| `transformers/examples/research_projects/distillation/training_configs/distilbert-base-uncased.json` | 26 | 277 |
| `transformers/examples/research_projects/distillation/training_configs/distilgpt2.json` | 16 | 152 |
| `transformers/examples/research_projects/distillation/training_configs/distilroberta-base.json` | 26 | 364 |
| `transformers/examples/research_projects/distillation/utils.py` | 456 | 4,280 |
| `transformers/examples/research_projects/fsner/README.md` | 476 | 3,531 |
| `transformers/examples/research_projects/fsner/pyproject.toml` | 11 | 142 |
| `transformers/examples/research_projects/fsner/requirements.txt` | 1 | 19 |
| `transformers/examples/research_projects/fsner/setup.py` | 49 | 864 |
| `transformers/examples/research_projects/fsner/src/fsner/__init__.py` | 12 | 129 |
| `transformers/examples/research_projects/fsner/src/fsner/model.py` | 285 | 3,100 |
| `transformers/examples/research_projects/fsner/src/fsner/tokenizer_utils.py` | 322 | 3,993 |
| `transformers/examples/research_projects/information-gain-filtration/README.md` | 739 | 5,273 |
| `transformers/examples/research_projects/information-gain-filtration/igf/__init__.py` | 0 | 0 |
| `transformers/examples/research_projects/information-gain-filtration/igf/igf.py` | 1,372 | 14,502 |
| `transformers/examples/research_projects/information-gain-filtration/requirements.txt` | 6 | 77 |
| `transformers/examples/research_projects/information-gain-filtration/result_igf.png` | — | 34,410 |
| `transformers/examples/research_projects/information-gain-filtration/run_clm_igf.py` | 1,496 | 15,498 |
| `transformers/examples/research_projects/jax-projects/HOW_TO_PROPOSE_PROJECT.md` | 1,013 | 7,138 |
| `transformers/examples/research_projects/jax-projects/README.md` | 10,965 | 83,740 |
| `transformers/examples/research_projects/jax-projects/big_bird/README.md` | 319 | 2,817 |
| `transformers/examples/research_projects/jax-projects/big_bird/bigbird_flax.py` | 911 | 11,714 |
| `transformers/examples/research_projects/jax-projects/big_bird/evaluate.py` | 607 | 6,464 |
| `transformers/examples/research_projects/jax-projects/big_bird/prepare_natural_questions.py` | 1,011 | 11,314 |
| `transformers/examples/research_projects/jax-projects/big_bird/requirements.txt` | 6 | 97 |
| `transformers/examples/research_projects/jax-projects/big_bird/sweep_flax.yaml` | 30 | 364 |
| `transformers/examples/research_projects/jax-projects/big_bird/train.py` | 198 | 2,815 |
| `transformers/examples/research_projects/jax-projects/dataset-streaming/README.md` | 576 | 4,724 |
| `transformers/examples/research_projects/jax-projects/dataset-streaming/run_mlm_flax_stream.py` | 2,546 | 26,574 |
| `transformers/examples/research_projects/jax-projects/hybrid_clip/README.md` | 927 | 7,474 |
| `transformers/examples/research_projects/jax-projects/hybrid_clip/configuration_hybrid_clip.py` | 361 | 4,397 |
| `transformers/examples/research_projects/jax-projects/hybrid_clip/modeling_hybrid_clip.py` | 1,469 | 18,051 |
| `transformers/examples/research_projects/jax-projects/hybrid_clip/requirements.txt` | 10 | 200 |
| `transformers/examples/research_projects/jax-projects/hybrid_clip/run_hybrid_clip.py` | 1,968 | 21,743 |
| `transformers/examples/research_projects/jax-projects/model_parallel/README.md` | 340 | 2,787 |
| `transformers/examples/research_projects/jax-projects/model_parallel/partitions.py` | 347 | 2,914 |
| `transformers/examples/research_projects/jax-projects/model_parallel/run_clm_mp.py` | 2,626 | 28,150 |
| `transformers/examples/research_projects/jax-projects/wav2vec2/README.md` | 533 | 4,590 |
| `transformers/examples/research_projects/jax-projects/wav2vec2/run_wav2vec2_pretrain_flax.py` | 2,010 | 25,029 |
| `transformers/examples/research_projects/layoutlmv3/README.md` | 350 | 2,931 |
| `transformers/examples/research_projects/layoutlmv3/requirements.txt` | 2 | 16 |
| `transformers/examples/research_projects/layoutlmv3/run_funsd_cord.py` | 1,911 | 21,214 |
| `transformers/examples/research_projects/longform-qa/README.md` | 60 | 664 |
| `transformers/examples/research_projects/longform-qa/eli5_app.py` | 1,256 | 13,474 |
| `transformers/examples/research_projects/longform-qa/eli5_utils.py` | 2,340 | 28,287 |
| `transformers/examples/research_projects/longform-qa/requirements.txt` | 6 | 52 |
| `transformers/examples/research_projects/luke/README.md` | 289 | 2,080 |
| `transformers/examples/research_projects/luke/luke_utils.py` | 526 | 5,106 |
| `transformers/examples/research_projects/luke/run_luke_ner_no_trainer.py` | 2,453 | 29,068 |
| `transformers/examples/research_projects/lxmert/README.md` | 27 | 189 |
| `transformers/examples/research_projects/lxmert/demo.ipynb` | 730 | 88,936 |
| `transformers/examples/research_projects/lxmert/extracting_data.py` | 403 | 5,254 |
| `transformers/examples/research_projects/lxmert/modeling_frcnn.py` | 6,655 | 73,736 |
| `transformers/examples/research_projects/lxmert/processing_image.py` | 543 | 5,678 |
| `transformers/examples/research_projects/lxmert/requirements.txt` | 98 | 1,665 |
| `transformers/examples/research_projects/lxmert/utils.py` | 1,612 | 18,212 |
| `transformers/examples/research_projects/lxmert/visualizing_image.py` | 1,129 | 13,420 |
| `transformers/examples/research_projects/mlm_wwm/README.md` | 469 | 3,606 |
| `transformers/examples/research_projects/mlm_wwm/requirements.txt` | 8 | 55 |
| `transformers/examples/research_projects/mlm_wwm/run_chinese_ref.py` | 595 | 5,282 |
| `transformers/examples/research_projects/mlm_wwm/run_mlm_wwm.py` | 1,735 | 18,252 |
| `transformers/examples/research_projects/mm-imdb/README.md` | 61 | 670 |
| `transformers/examples/research_projects/mm-imdb/run_mmimdb.py` | 2,073 | 23,952 |
| `transformers/examples/research_projects/mm-imdb/utils_mmimdb.py` | 425 | 4,586 |
| `transformers/examples/research_projects/movement-pruning/README.md` | 1,242 | 11,324 |
| `transformers/examples/research_projects/movement-pruning/Saving_PruneBERT.ipynb` | 2,192 | 27,952 |
| `transformers/examples/research_projects/movement-pruning/bertarize.py` | 488 | 5,157 |
| `transformers/examples/research_projects/movement-pruning/counts_parameters.py` | 381 | 3,466 |
| `transformers/examples/research_projects/movement-pruning/emmental/__init__.py` | 21 | 301 |
| `transformers/examples/research_projects/movement-pruning/emmental/configuration_bert_masked.py` | 232 | 2,549 |
| `transformers/examples/research_projects/movement-pruning/emmental/modeling_bert_masked.py` | 3,910 | 47,081 |
| `transformers/examples/research_projects/movement-pruning/emmental/modules/__init__.py` | 13 | 128 |
| `transformers/examples/research_projects/movement-pruning/emmental/modules/binarizer.py` | 704 | 5,822 |
| `transformers/examples/research_projects/movement-pruning/emmental/modules/masked_nn.py` | 474 | 4,506 |
| `transformers/examples/research_projects/movement-pruning/masked_run_glue.py` | 3,406 | 40,733 |
| `transformers/examples/research_projects/movement-pruning/masked_run_squad.py` | 3,920 | 47,888 |
| `transformers/examples/research_projects/movement-pruning/requirements.txt` | 7 | 186 |
| `transformers/examples/research_projects/onnx/summarization/README.md` | 251 | 1,738 |
| `transformers/examples/research_projects/onnx/summarization/bart_onnx/generation_onnx.py` | 2,345 | 30,835 |
| `transformers/examples/research_projects/onnx/summarization/bart_onnx/reduce_onnx_size.py` | 316 | 3,576 |
| `transformers/examples/research_projects/onnx/summarization/requirements.txt` | 3 | 13 |
| `transformers/examples/research_projects/onnx/summarization/run_onnx_exporter.py` | 530 | 6,705 |
| `transformers/examples/research_projects/performer/README.md` | 171 | 1,348 |
| `transformers/examples/research_projects/performer/full_script.sh` | 24 | 351 |
| `transformers/examples/research_projects/performer/modeling_flax_performer.py` | 1,837 | 21,123 |
| `transformers/examples/research_projects/performer/modeling_flax_performer_utils.py` | 2,289 | 25,680 |
| `transformers/examples/research_projects/performer/run_mlm_performer.py` | 2,811 | 28,616 |
| `transformers/examples/research_projects/performer/sanity_script.sh` | 24 | 353 |
| `transformers/examples/research_projects/pplm/README.md` | 296 | 2,396 |
| `transformers/examples/research_projects/pplm/imgs/headfigure.png` | — | 668,261 |
| `transformers/examples/research_projects/pplm/imgs/wooly.png` | — | 679,776 |
| `transformers/examples/research_projects/pplm/pplm_classification_head.py` | 52 | 651 |
| `transformers/examples/research_projects/pplm/requirements.txt` | 26 | 265 |
| `transformers/examples/research_projects/pplm/run_pplm.py` | 2,272 | 29,044 |
| `transformers/examples/research_projects/pplm/run_pplm_discrim_train.py` | 1,493 | 18,797 |
| `transformers/examples/research_projects/quantization-qdqbert/Dockerfile` | 172 | 1,250 |
| `transformers/examples/research_projects/quantization-qdqbert/README.md` | 687 | 5,900 |
| `transformers/examples/research_projects/quantization-qdqbert/evaluate-hf-trt-qa.py` | 1,768 | 17,856 |
| `transformers/examples/research_projects/quantization-qdqbert/ort-infer-benchmark.py` | 119 | 1,485 |
| `transformers/examples/research_projects/quantization-qdqbert/quant_trainer.py` | 1,032 | 12,327 |
| `transformers/examples/research_projects/quantization-qdqbert/run_quant_qa.py` | 2,920 | 31,741 |
| `transformers/examples/research_projects/quantization-qdqbert/trainer_quant_qa.py` | 683 | 8,655 |
| `transformers/examples/research_projects/quantization-qdqbert/utils_qa.py` | 2,258 | 22,378 |
| `transformers/examples/research_projects/rag-end2end-retriever/README.md` | 435 | 3,519 |
| `transformers/examples/research_projects/rag-end2end-retriever/callbacks_rag.py` | 377 | 4,474 |
| `transformers/examples/research_projects/rag-end2end-retriever/distributed_ray_retriever.py` | 663 | 8,211 |
| `transformers/examples/research_projects/rag-end2end-retriever/eval_rag.py` | 884 | 11,211 |
| `transformers/examples/research_projects/rag-end2end-retriever/finetune_rag.py` | 2,450 | 33,695 |
| `transformers/examples/research_projects/rag-end2end-retriever/finetune_rag_ray_end2end.sh` | 216 | 2,069 |
| `transformers/examples/research_projects/rag-end2end-retriever/kb_encode_utils.py` | 267 | 3,179 |
| `transformers/examples/research_projects/rag-end2end-retriever/lightning_base.py` | 1,168 | 16,087 |
| `transformers/examples/research_projects/rag-end2end-retriever/requirements.txt` | 19 | 127 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/dummy-kb/my_knowledge_dataset.csv` | 590 | 3,592 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/dummy-train-data/train.source` | 306 | 1,583 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/dummy-train-data/train.target` | 192 | 1,157 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/dummy-train-data/val.source` | 51 | 263 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/dummy-train-data/val.target` | 32 | 192 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/test_finetune.sh` | 161 | 1,506 |
| `transformers/examples/research_projects/rag-end2end-retriever/test_run/test_rag_new_features.sh` | 32 | 363 |
| `transformers/examples/research_projects/rag-end2end-retriever/use_own_knowledge_dataset.py` | 646 | 6,992 |
| `transformers/examples/research_projects/rag-end2end-retriever/utils_rag.py` | 680 | 8,114 |
| `transformers/examples/research_projects/rag/README.md` | 1,255 | 10,437 |
| `transformers/examples/research_projects/rag/__init__.py` | 6 | 87 |
| `transformers/examples/research_projects/rag/_test_finetune_rag.py` | 258 | 3,953 |
| `transformers/examples/research_projects/rag/callbacks_rag.py` | 378 | 4,443 |
| `transformers/examples/research_projects/rag/consolidate_rag_checkpoint.py` | 245 | 3,679 |
| `transformers/examples/research_projects/rag/distributed_pytorch_retriever.py` | 600 | 6,539 |
| `transformers/examples/research_projects/rag/distributed_ray_retriever.py` | 587 | 7,185 |
| `transformers/examples/research_projects/rag/eval_rag.py` | 884 | 11,211 |
| `transformers/examples/research_projects/rag/finetune_rag.py` | 1,946 | 26,214 |
| `transformers/examples/research_projects/rag/finetune_rag.sh` | 115 | 1,036 |
| `transformers/examples/research_projects/rag/finetune_rag_ray.sh` | 147 | 1,261 |
| `transformers/examples/research_projects/rag/lightning_base.py` | 1,128 | 15,637 |
| `transformers/examples/research_projects/rag/parse_dpr_relevance_data.py` | 134 | 1,353 |
| `transformers/examples/research_projects/rag/requirements.txt` | 20 | 132 |
| `transformers/examples/research_projects/rag/test_data/my_knowledge_dataset.csv` | 590 | 3,592 |
| `transformers/examples/research_projects/rag/test_distributed_retriever.py` | 774 | 13,794 |
| `transformers/examples/research_projects/rag/use_own_knowledge_dataset.py` | 737 | 8,257 |
| `transformers/examples/research_projects/rag/utils_rag.py` | 680 | 8,114 |
| `transformers/examples/research_projects/robust-speech-event/README.md` | 5,585 | 42,307 |
| `transformers/examples/research_projects/robust-speech-event/eval.py` | 457 | 4,734 |
| `transformers/examples/research_projects/robust-speech-event/run_speech_recognition_ctc_bnb.py` | 2,914 | 31,631 |
| `transformers/examples/research_projects/robust-speech-event/run_speech_recognition_ctc_streaming.py` | 2,562 | 28,274 |
| `transformers/examples/research_projects/self-training-text-classification/README.md` | 783 | 6,776 |
| `transformers/examples/research_projects/self-training-text-classification/finetuning.py` | 2,940 | 34,604 |
| `transformers/examples/research_projects/self-training-text-classification/requirements.txt` | 13 | 94 |
| `transformers/examples/research_projects/self-training-text-classification/run.sh` | 260 | 2,553 |
| `transformers/examples/research_projects/self-training-text-classification/selftraining.py` | 1,402 | 16,963 |
| `transformers/examples/research_projects/seq2seq-distillation/README.md` | 2,440 | 19,761 |
| `transformers/examples/research_projects/seq2seq-distillation/_test_bash_script.py` | 621 | 8,363 |
| `transformers/examples/research_projects/seq2seq-distillation/_test_make_student.py` | 88 | 1,602 |
| `transformers/examples/research_projects/seq2seq-distillation/_test_seq2seq_examples.py` | 1,136 | 16,561 |
| `transformers/examples/research_projects/seq2seq-distillation/_test_seq2seq_examples_multi_gpu.py` | 445 | 5,672 |
| `transformers/examples/research_projects/seq2seq-distillation/callbacks.py` | 371 | 4,431 |
| `transformers/examples/research_projects/seq2seq-distillation/convert_pl_checkpoint_to_hf.py` | 254 | 2,478 |
| `transformers/examples/research_projects/seq2seq-distillation/distil_marian_enro_teacher.sh` | 65 | 764 |
| `transformers/examples/research_projects/seq2seq-distillation/distil_marian_no_teacher.sh` | 59 | 657 |
| `transformers/examples/research_projects/seq2seq-distillation/distillation.py` | 1,056 | 14,607 |
| `transformers/examples/research_projects/seq2seq-distillation/dynamic_bs_example.sh` | 55 | 630 |
| `transformers/examples/research_projects/seq2seq-distillation/finetune.py` | 1,353 | 19,055 |
| `transformers/examples/research_projects/seq2seq-distillation/finetune.sh` | 48 | 342 |
| `transformers/examples/research_projects/seq2seq-distillation/finetune_bart_tiny.sh` | 90 | 848 |
| `transformers/examples/research_projects/seq2seq-distillation/finetune_pegasus_xsum.sh` | 53 | 500 |
| `transformers/examples/research_projects/seq2seq-distillation/finetune_t5.sh` | 36 | 371 |
| `transformers/examples/research_projects/seq2seq-distillation/lightning_base.py` | 1,058 | 15,050 |
| `transformers/examples/research_projects/seq2seq-distillation/make_student.py` | 859 | 8,208 |
| `transformers/examples/research_projects/seq2seq-distillation/precomputed_pseudo_labels.md` | 304 | 3,791 |
| `transformers/examples/research_projects/seq2seq-distillation/requirements.txt` | 24 | 237 |
| `transformers/examples/research_projects/seq2seq-distillation/run_eval.py` | 579 | 6,546 |
| `transformers/examples/research_projects/seq2seq-distillation/sentence_splitter.py` | 70 | 633 |
| `transformers/examples/research_projects/seq2seq-distillation/train_distilbart_cnn.sh` | 57 | 649 |
| `transformers/examples/research_projects/seq2seq-distillation/train_distilbart_xsum.sh` | 64 | 777 |
| `transformers/examples/research_projects/seq2seq-distillation/train_mbart_cc25_enro.sh` | 51 | 598 |
| `transformers/examples/research_projects/seq2seq-distillation/utils.py` | 2,102 | 24,333 |
| `transformers/examples/research_projects/tapex/README.md` | 1,544 | 11,905 |
| `transformers/examples/research_projects/tapex/requirements.txt` | 4 | 26 |
| `transformers/examples/research_projects/tapex/run_tabfact_with_tapex.py` | 1,858 | 19,890 |
| `transformers/examples/research_projects/tapex/run_wikisql_with_tapex.py` | 2,394 | 26,715 |
| `transformers/examples/research_projects/tapex/run_wikitablequestions_with_tapex.py` | 2,289 | 25,496 |
| `transformers/examples/research_projects/tapex/wikisql_utils.py` | 846 | 8,066 |
| `transformers/examples/research_projects/visual_bert/README.md` | 43 | 387 |
| `transformers/examples/research_projects/visual_bert/demo.ipynb` | 723 | 90,635 |
| `transformers/examples/research_projects/visual_bert/extracting_data.py` | 403 | 5,254 |
| `transformers/examples/research_projects/visual_bert/modeling_frcnn.py` | 6,655 | 73,736 |
| `transformers/examples/research_projects/visual_bert/processing_image.py` | 543 | 5,678 |
| `transformers/examples/research_projects/visual_bert/requirements.txt` | 98 | 1,665 |
| `transformers/examples/research_projects/visual_bert/utils.py` | 1,612 | 18,212 |
| `transformers/examples/research_projects/visual_bert/visualizing_image.py` | 1,129 | 13,420 |
| `transformers/examples/research_projects/wav2vec2/FINE_TUNE_XLSR_WAV2VEC2.md` | 4,391 | 32,821 |
| `transformers/examples/research_projects/wav2vec2/README.md` | 871 | 9,073 |
| `transformers/examples/research_projects/wav2vec2/ds_config_wav2vec2_zero2.json` | 85 | 1,222 |
| `transformers/examples/research_projects/wav2vec2/ds_config_wav2vec2_zero3.json` | 96 | 1,451 |
| `transformers/examples/research_projects/wav2vec2/finetune_base_100.sh` | 42 | 587 |
| `transformers/examples/research_projects/wav2vec2/finetune_base_timit_asr.sh` | 45 | 610 |
| `transformers/examples/research_projects/wav2vec2/finetune_large_lv60_100.sh` | 42 | 599 |
| `transformers/examples/research_projects/wav2vec2/finetune_large_lv60_timit_asr.sh` | 47 | 656 |
| `transformers/examples/research_projects/wav2vec2/finetune_large_xlsr_53_arabic_speech_corpus.sh` | 51 | 771 |
| `transformers/examples/research_projects/wav2vec2/finetune_wav2vec2_xlsr_turkish.sh` | 45 | 677 |
| `transformers/examples/research_projects/wav2vec2/requirements.txt` | 7 | 92 |
| `transformers/examples/research_projects/wav2vec2/run_asr.py` | 1,630 | 19,904 |
| `transformers/examples/research_projects/wav2vec2/run_common_voice.py` | 1,662 | 19,837 |
| `transformers/examples/research_projects/wav2vec2/run_pretrain.py` | 1,291 | 15,658 |
| `transformers/examples/research_projects/wav2vec2/test_wav2vec2_deepspeed.py` | 605 | 6,502 |
| `transformers/examples/research_projects/wav2vec2/vocab/buckwalter.json` | 114 | 733 |
| `transformers/examples/research_projects/xtreme-s/README.md` | 791 | 7,785 |
| `transformers/examples/research_projects/xtreme-s/requirements.txt` | 9 | 57 |
| `transformers/examples/research_projects/xtreme-s/run_xtreme_s.py` | 3,354 | 38,730 |
| `transformers/examples/research_projects/zero-shot-distillation/README.md` | 1,145 | 8,828 |
| `transformers/examples/research_projects/zero-shot-distillation/distill_classifier.py` | 1,102 | 12,205 |
| `transformers/examples/tensorflow/README.md` | 306 | 2,674 |
| `transformers/examples/tensorflow/benchmarking/README.md` | 175 | 1,654 |
| `transformers/examples/tensorflow/benchmarking/plot_csv_file.py` | 564 | 6,407 |
| `transformers/examples/tensorflow/benchmarking/requirements.txt` | 3 | 17 |
| `transformers/examples/tensorflow/benchmarking/run_benchmark_tf.py` | 212 | 1,915 |
| `transformers/examples/tensorflow/language-modeling/README.md` | 451 | 3,090 |
| `transformers/examples/tensorflow/language-modeling/requirements.txt` | 6 | 41 |
| `transformers/examples/tensorflow/language-modeling/run_clm.py` | 2,237 | 23,558 |
| `transformers/examples/tensorflow/language-modeling/run_mlm.py` | 2,416 | 25,905 |
| `transformers/examples/tensorflow/multiple-choice/README.md` | 305 | 1,989 |
| `transformers/examples/tensorflow/multiple-choice/requirements.txt` | 7 | 51 |
| `transformers/examples/tensorflow/multiple-choice/run_swag.py` | 2,062 | 22,101 |
| `transformers/examples/tensorflow/question-answering/README.md` | 415 | 2,631 |
| `transformers/examples/tensorflow/question-answering/requirements.txt` | 6 | 38 |
| `transformers/examples/tensorflow/question-answering/run_qa.py` | 2,966 | 31,684 |
| `transformers/examples/tensorflow/question-answering/utils_qa.py` | 2,297 | 22,777 |
| `transformers/examples/tensorflow/summarization/README.md` | 212 | 1,472 |
| `transformers/examples/tensorflow/summarization/run_summarization.py` | 2,658 | 28,683 |
| `transformers/examples/tensorflow/text-classification/README.md` | 1,050 | 6,669 |
| `transformers/examples/tensorflow/text-classification/requirements.txt` | 10 | 68 |
| `transformers/examples/tensorflow/text-classification/run_glue.py` | 2,014 | 22,568 |
| `transformers/examples/tensorflow/text-classification/run_text_classification.py` | 2,155 | 21,899 |
| `transformers/examples/tensorflow/token-classification/README.md` | 259 | 1,992 |
| `transformers/examples/tensorflow/token-classification/run_ner.py` | 2,178 | 23,041 |
| `transformers/examples/tensorflow/translation/README.md` | 378 | 2,893 |
| `transformers/examples/tensorflow/translation/run_translation.py` | 2,508 | 27,696 |
| `transformers/hubconf.py` | 643 | 8,496 |
| `transformers/model_cards/README.md` | 180 | 1,141 |
| `transformers/notebooks/README.md` | 1,296 | 23,493 |
| `transformers/pyproject.toml` | 7 | 57 |
| `transformers/scripts/benchmark/trainer-benchmark.py` | 1,802 | 15,569 |
| `transformers/scripts/check_tokenizers.py` | 601 | 5,547 |
| `transformers/scripts/distributed/torch-distributed-gpu-test.py` | 363 | 3,009 |
| `transformers/scripts/fsmt/convert-allenai-wmt16.sh` | 308 | 3,282 |
| `transformers/scripts/fsmt/convert-allenai-wmt19.sh` | 271 | 2,411 |
| `transformers/scripts/fsmt/convert-facebook-wmt19.sh` | 312 | 3,030 |
| `transformers/scripts/fsmt/eval-allenai-wmt16.sh` | 376 | 3,758 |
| `transformers/scripts/fsmt/eval-allenai-wmt19.sh` | 333 | 3,024 |
| `transformers/scripts/fsmt/eval-facebook-wmt19.sh` | 682 | 6,673 |
| `transformers/scripts/fsmt/fsmt-make-super-tiny-model.py` | 391 | 3,263 |
| `transformers/scripts/fsmt/fsmt-make-tiny-model.py` | 289 | 2,179 |
| `transformers/scripts/fsmt/gen-card-allenai-wmt16.py` | 521 | 4,908 |
| `transformers/scripts/fsmt/gen-card-allenai-wmt19.py` | 477 | 4,490 |
| `transformers/scripts/fsmt/gen-card-facebook-wmt19.py` | 570 | 5,510 |
| `transformers/scripts/fsmt/s3-move.sh` | 466 | 4,974 |
| `transformers/scripts/fsmt/tests-to-run.sh` | 135 | 1,093 |
| `transformers/scripts/pegasus/build_test_sample_spm_no_bos.py` | 172 | 1,252 |
| `transformers/scripts/stale.py` | 314 | 2,626 |
| `transformers/scripts/tatoeba/README.md` | 272 | 2,384 |
| `transformers/scripts/tatoeba/upload_models.sh` | 35 | 292 |
| `transformers/setup.cfg` | 80 | 874 |
| `transformers/setup.py` | 1,527 | 14,669 |
| `transformers/src/transformers/__init__.py` | 7,559 | 190,834 |
| `transformers/src/transformers/activations.py` | 723 | 6,612 |
| `transformers/src/transformers/activations_tf.py` | 544 | 4,313 |
| `transformers/src/transformers/benchmark/__init__.py` | 0 | 0 |
| `transformers/src/transformers/benchmark/benchmark.py` | 861 | 10,753 |
| `transformers/src/transformers/benchmark/benchmark_args.py` | 352 | 3,778 |
| `transformers/src/transformers/benchmark/benchmark_args_tf.py` | 398 | 4,592 |
| `transformers/src/transformers/benchmark/benchmark_args_utils.py` | 717 | 6,425 |
| `transformers/src/transformers/benchmark/benchmark_tf.py` | 1,081 | 13,066 |
| `transformers/src/transformers/benchmark/benchmark_utils.py` | 3,419 | 37,626 |
| `transformers/src/transformers/commands/__init__.py` | 122 | 923 |
| `transformers/src/transformers/commands/add_new_model.py` | 780 | 11,064 |
| `transformers/src/transformers/commands/add_new_model_like.py` | 6,114 | 64,497 |
| `transformers/src/transformers/commands/convert.py` | 527 | 7,856 |
| `transformers/src/transformers/commands/download.py` | 188 | 1,860 |
| `transformers/src/transformers/commands/env.py` | 311 | 3,310 |
| `transformers/src/transformers/commands/lfs.py` | 748 | 8,001 |
| `transformers/src/transformers/commands/pt_to_tf.py` | 1,170 | 13,799 |
| `transformers/src/transformers/commands/run.py` | 400 | 4,249 |
| `transformers/src/transformers/commands/serving.py` | 657 | 8,027 |
| `transformers/src/transformers/commands/train.py` | 509 | 6,329 |
| `transformers/src/transformers/commands/transformers_cli.py` | 196 | 2,047 |
| `transformers/src/transformers/commands/user.py` | 652 | 7,149 |
| `transformers/src/transformers/configuration_utils.py` | 4,947 | 47,888 |
| `transformers/src/transformers/convert_graph_to_onnx.py` | 1,989 | 19,585 |
| `transformers/src/transformers/convert_pytorch_checkpoint_to_tf2.py` | 1,006 | 16,732 |
| `transformers/src/transformers/convert_slow_tokenizer.py` | 2,532 | 39,731 |
| `transformers/src/transformers/convert_slow_tokenizers_checkpoints_to_fast.py` | 415 | 4,982 |
| `transformers/src/transformers/convert_tf_hub_seq_to_seq_bert_to_pytorch.py` | 257 | 2,899 |
| `transformers/src/transformers/data/__init__.py` | 170 | 1,594 |
| `transformers/src/transformers/data/data_collator.py` | 8,043 | 76,857 |
| `transformers/src/transformers/data/datasets/__init__.py` | 150 | 1,080 |
| `transformers/src/transformers/data/datasets/glue.py` | 600 | 6,165 |
| `transformers/src/transformers/data/datasets/language_modeling.py` | 2,164 | 23,723 |
| `transformers/src/transformers/data/datasets/squad.py` | 846 | 9,220 |
| `transformers/src/transformers/data/metrics/__init__.py` | 378 | 3,776 |
| `transformers/src/transformers/data/metrics/squad_metrics.py` | 2,607 | 29,601 |
| `transformers/src/transformers/data/processors/__init__.py` | 158 | 1,185 |
| `transformers/src/transformers/data/processors/glue.py` | 1,822 | 23,219 |
| `transformers/src/transformers/data/processors/squad.py` | 2,718 | 33,154 |
| `transformers/src/transformers/data/processors/utils.py` | 1,292 | 13,829 |
| `transformers/src/transformers/data/processors/xnli.py` | 362 | 3,489 |
| `transformers/src/transformers/data/test_generation_utils.py` | 340 | 3,433 |
| `transformers/src/transformers/debug_utils.py` | 1,410 | 12,907 |
| `transformers/src/transformers/deepspeed.py` | 1,572 | 15,835 |
| `transformers/src/transformers/dependency_versions_check.py` | 221 | 1,756 |
| `transformers/src/transformers/dependency_versions_table.py` | 165 | 2,511 |
| `transformers/src/transformers/dynamic_module_utils.py` | 2,040 | 19,306 |
| `transformers/src/transformers/feature_extraction_sequence_utils.py` | 1,760 | 18,089 |
| `transformers/src/transformers/feature_extraction_utils.py` | 2,478 | 26,855 |
| `transformers/src/transformers/file_utils.py` | 296 | 3,953 |
| `transformers/src/transformers/generation_beam_constraints.py` | 1,914 | 19,097 |
| `transformers/src/transformers/generation_beam_search.py` | 3,708 | 41,551 |
| `transformers/src/transformers/generation_flax_logits_process.py` | 1,115 | 10,879 |
| `transformers/src/transformers/generation_flax_utils.py` | 3,377 | 38,980 |
| `transformers/src/transformers/generation_logits_process.py` | 2,989 | 30,983 |
| `transformers/src/transformers/generation_stopping_criteria.py` | 512 | 5,509 |
| `transformers/src/transformers/generation_tf_logits_process.py` | 2,307 | 23,394 |
| `transformers/src/transformers/generation_tf_utils.py` | 13,921 | 162,561 |
| `transformers/src/transformers/generation_utils.py` | 14,749 | 178,650 |
| `transformers/src/transformers/hf_argparser.py` | 1,273 | 12,094 |
| `transformers/src/transformers/image_utils.py` | 1,624 | 14,709 |
| `transformers/src/transformers/integrations.py` | 3,594 | 43,625 |
| `transformers/src/transformers/keras_callbacks.py` | 1,865 | 18,902 |
| `transformers/src/transformers/modelcard.py` | 3,079 | 35,352 |
| `transformers/src/transformers/modeling_flax_outputs.py` | 3,892 | 38,967 |
| `transformers/src/transformers/modeling_flax_pytorch_utils.py` | 1,185 | 12,341 |
| `transformers/src/transformers/modeling_flax_utils.py` | 4,998 | 51,333 |
| `transformers/src/transformers/modeling_outputs.py` | 6,324 | 63,666 |
| `transformers/src/transformers/modeling_tf_outputs.py` | 4,994 | 48,017 |
| `transformers/src/transformers/modeling_tf_pytorch_utils.py` | 2,040 | 20,136 |
| `transformers/src/transformers/modeling_tf_utils.py` | 12,005 | 125,495 |
| `transformers/src/transformers/modeling_utils.py` | 13,458 | 142,127 |
| `transformers/src/transformers/models/__init__.py` | 268 | 2,628 |
| `transformers/src/transformers/models/albert/__init__.py` | 368 | 5,653 |
| `transformers/src/transformers/models/albert/configuration_albert.py` | 776 | 8,545 |
| `transformers/src/transformers/models/albert/convert_albert_original_tf_checkpoint_to_pytorch.py` | 220 | 2,183 |
| `transformers/src/transformers/models/albert/modeling_albert.py` | 4,858 | 61,295 |
| `transformers/src/transformers/models/albert/modeling_flax_albert.py` | 2,950 | 40,946 |
| `transformers/src/transformers/models/albert/modeling_tf_albert.py` | 4,958 | 65,328 |
| `transformers/src/transformers/models/albert/tokenization_albert.py` | 1,428 | 14,707 |
| `transformers/src/transformers/models/albert/tokenization_albert_fast.py` | 1,031 | 10,814 |
| `transformers/src/transformers/models/auto/__init__.py` | 498 | 12,456 |
| `transformers/src/transformers/models/auto/auto_factory.py` | 3,627 | 35,648 |
| `transformers/src/transformers/models/auto/configuration_auto.py` | 2,376 | 32,772 |
| `transformers/src/transformers/models/auto/feature_extraction_auto.py` | 1,660 | 17,373 |
| `transformers/src/transformers/models/auto/modeling_auto.py` | 1,997 | 39,661 |
| `transformers/src/transformers/models/auto/modeling_flax_auto.py` | 699 | 12,752 |
| `transformers/src/transformers/models/auto/modeling_tf_auto.py` | 1,160 | 21,730 |
| `transformers/src/transformers/models/auto/processing_auto.py` | 1,255 | 13,097 |
| `transformers/src/transformers/models/auto/tokenization_auto.py` | 2,798 | 33,551 |
| `transformers/src/transformers/models/bart/__init__.py` | 322 | 4,336 |
| `transformers/src/transformers/models/bart/configuration_bart.py` | 1,547 | 18,973 |
| `transformers/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py` | 434 | 5,647 |
| `transformers/src/transformers/models/bart/modeling_bart.py` | 7,182 | 88,338 |
| `transformers/src/transformers/models/bart/modeling_flax_bart.py` | 6,160 | 82,688 |
| `transformers/src/transformers/models/bart/modeling_tf_bart.py` | 5,844 | 71,171 |
| `transformers/src/transformers/models/bart/tokenization_bart.py` | 1,832 | 17,972 |
| `transformers/src/transformers/models/bart/tokenization_bart_fast.py` | 1,249 | 13,803 |
| `transformers/src/transformers/models/barthez/__init__.py` | 209 | 2,020 |
| `transformers/src/transformers/models/barthez/tokenization_barthez.py` | 1,245 | 12,559 |
| `transformers/src/transformers/models/barthez/tokenization_barthez_fast.py` | 879 | 8,899 |
| `transformers/src/transformers/models/bartpho/__init__.py` | 181 | 1,533 |
| `transformers/src/transformers/models/bartpho/tokenization_bartpho.py` | 1,376 | 14,218 |
| `transformers/src/transformers/models/beit/__init__.py` | 272 | 3,326 |
| `transformers/src/transformers/models/beit/configuration_beit.py` | 924 | 9,624 |
| `transformers/src/transformers/models/beit/convert_beit_unilm_to_pytorch.py` | 1,223 | 16,351 |
| `transformers/src/transformers/models/beit/feature_extraction_beit.py` | 1,056 | 10,266 |
| `transformers/src/transformers/models/beit/modeling_beit.py` | 4,458 | 53,496 |
| `transformers/src/transformers/models/beit/modeling_flax_beit.py` | 2,914 | 37,032 |
| `transformers/src/transformers/models/bert/__init__.py` | 366 | 5,745 |
| `transformers/src/transformers/models/bert/configuration_bert.py` | 781 | 9,961 |
| `transformers/src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py` | 915 | 10,490 |
| `transformers/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py` | 220 | 2,159 |
| `transformers/src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py` | 345 | 4,101 |
| `transformers/src/transformers/models/bert/modeling_bert.py` | 6,616 | 83,984 |
| `transformers/src/transformers/models/bert/modeling_flax_bert.py` | 4,492 | 61,477 |
| `transformers/src/transformers/models/bert/modeling_tf_bert.py` | 7,131 | 92,857 |
| `transformers/src/transformers/models/bert/tokenization_bert.py` | 2,186 | 24,517 |
| `transformers/src/transformers/models/bert/tokenization_bert_fast.py` | 1,040 | 14,870 |
| `transformers/src/transformers/models/bert_generation/__init__.py` | 224 | 2,446 |
| `transformers/src/transformers/models/bert_generation/configuration_bert_generation.py` | 600 | 6,039 |
| `transformers/src/transformers/models/bert_generation/modeling_bert_generation.py` | 2,449 | 27,712 |
| `transformers/src/transformers/models/bert_generation/tokenization_bert_generation.py` | 618 | 6,719 |
| `transformers/src/transformers/models/bert_japanese/__init__.py` | 161 | 1,224 |
| `transformers/src/transformers/models/bert_japanese/tokenization_bert_japanese.py` | 1,010 | 13,221 |
| `transformers/src/transformers/models/bertweet/__init__.py` | 157 | 1,130 |
| `transformers/src/transformers/models/bertweet/tokenization_bertweet.py` | 2,786 | 27,205 |
| `transformers/src/transformers/models/big_bird/__init__.py` | 325 | 4,745 |
| `transformers/src/transformers/models/big_bird/configuration_big_bird.py` | 775 | 8,231 |
| `transformers/src/transformers/models/big_bird/convert_bigbird_original_tf_checkpoint_to_pytorch.py` | 241 | 2,494 |
| `transformers/src/transformers/models/big_bird/modeling_big_bird.py` | 11,402 | 142,432 |
| `transformers/src/transformers/models/big_bird/modeling_flax_big_bird.py` | 7,876 | 104,503 |
| `transformers/src/transformers/models/big_bird/tokenization_big_bird.py` | 1,237 | 12,363 |
| `transformers/src/transformers/models/big_bird/tokenization_big_bird_fast.py` | 1,168 | 11,365 |
| `transformers/src/transformers/models/bigbird_pegasus/__init__.py` | 212 | 2,487 |
| `transformers/src/transformers/models/bigbird_pegasus/configuration_bigbird_pegasus.py` | 1,586 | 19,808 |
| `transformers/src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py` | 573 | 6,295 |
| `transformers/src/transformers/models/bigbird_pegasus/modeling_bigbird_pegasus.py` | 11,823 | 146,295 |
| `transformers/src/transformers/models/blenderbot/__init__.py` | 316 | 4,202 |
| `transformers/src/transformers/models/blenderbot/configuration_blenderbot.py` | 1,513 | 19,193 |
| `transformers/src/transformers/models/blenderbot/convert_blenderbot_original_pytorch_checkpoint_to_pytorch.py` | 334 | 3,702 |
| `transformers/src/transformers/models/blenderbot/modeling_blenderbot.py` | 6,256 | 76,301 |
| `transformers/src/transformers/models/blenderbot/modeling_flax_blenderbot.py` | 4,829 | 65,088 |
| `transformers/src/transformers/models/blenderbot/modeling_tf_blenderbot.py` | 5,572 | 68,458 |
| `transformers/src/transformers/models/blenderbot/tokenization_blenderbot.py` | 410 | 4,064 |
| `transformers/src/transformers/models/blenderbot/tokenization_blenderbot_fast.py` | 381 | 3,918 |
| `transformers/src/transformers/models/blenderbot_small/__init__.py` | 316 | 4,434 |
| `transformers/src/transformers/models/blenderbot_small/configuration_blenderbot_small.py` | 1,493 | 18,656 |
| `transformers/src/transformers/models/blenderbot_small/modeling_blenderbot_small.py` | 6,161 | 75,188 |
| `transformers/src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py` | 4,872 | 66,119 |
| `transformers/src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py` | 5,499 | 67,354 |
| `transformers/src/transformers/models/blenderbot_small/tokenization_blenderbot_small.py` | 813 | 8,647 |
| `transformers/src/transformers/models/blenderbot_small/tokenization_blenderbot_small_fast.py` | 358 | 4,057 |
| `transformers/src/transformers/models/bloom/__init__.py` | 234 | 2,581 |
| `transformers/src/transformers/models/bloom/configuration_bloom.py` | 787 | 7,872 |
| `transformers/src/transformers/models/bloom/convert_bloom_original_checkpoint_to_pytorch.py` | 832 | 10,092 |
| `transformers/src/transformers/models/bloom/modeling_bloom.py` | 4,024 | 47,883 |
| `transformers/src/transformers/models/bloom/tokenization_bloom_fast.py` | 641 | 7,267 |
| `transformers/src/transformers/models/bort/__init__.py` | 0 | 0 |
| `transformers/src/transformers/models/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py` | 904 | 14,057 |
| `transformers/src/transformers/models/byt5/__init__.py` | 157 | 1,113 |
| `transformers/src/transformers/models/byt5/convert_byt5_original_tf_checkpoint_to_pytorch.py` | 219 | 2,120 |
| `transformers/src/transformers/models/byt5/tokenization_byt5.py` | 1,101 | 10,726 |
| `transformers/src/transformers/models/camembert/__init__.py` | 314 | 4,462 |
| `transformers/src/transformers/models/camembert/configuration_camembert.py` | 232 | 2,241 |
| `transformers/src/transformers/models/camembert/modeling_camembert.py` | 586 | 5,503 |
| `transformers/src/transformers/models/camembert/modeling_tf_camembert.py` | 731 | 6,451 |
| `transformers/src/transformers/models/camembert/tokenization_camembert.py` | 1,312 | 12,947 |
| `transformers/src/transformers/models/camembert/tokenization_camembert_fast.py` | 896 | 8,657 |
| `transformers/src/transformers/models/canine/__init__.py` | 217 | 2,443 |
| `transformers/src/transformers/models/canine/configuration_canine.py` | 646 | 6,548 |
| `transformers/src/transformers/models/canine/convert_canine_original_tf_checkpoint_to_pytorch.py` | 217 | 2,118 |
| `transformers/src/transformers/models/canine/modeling_canine.py` | 5,951 | 72,749 |
| `transformers/src/transformers/models/canine/tokenization_canine.py` | 1,008 | 9,275 |
| `transformers/src/transformers/models/clip/__init__.py` | 359 | 4,793 |
| `transformers/src/transformers/models/clip/configuration_clip.py` | 1,371 | 14,347 |
| `transformers/src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py` | 399 | 5,248 |
| `transformers/src/transformers/models/clip/feature_extraction_clip.py` | 791 | 7,310 |
| `transformers/src/transformers/models/clip/modeling_clip.py` | 3,643 | 46,042 |
| `transformers/src/transformers/models/clip/modeling_flax_clip.py` | 3,513 | 45,832 |
| `transformers/src/transformers/models/clip/modeling_tf_clip.py` | 4,459 | 56,541 |
| `transformers/src/transformers/models/clip/processing_clip.py` | 610 | 5,383 |
| `transformers/src/transformers/models/clip/tokenization_clip.py` | 1,405 | 13,888 |
| `transformers/src/transformers/models/clip/tokenization_clip_fast.py` | 673 | 6,953 |
| `transformers/src/transformers/models/codegen/__init__.py` | 240 | 2,614 |
| `transformers/src/transformers/models/codegen/configuration_codegen.py` | 892 | 10,526 |
| `transformers/src/transformers/models/codegen/modeling_codegen.py` | 2,735 | 31,481 |
| `transformers/src/transformers/models/codegen/tokenization_codegen.py` | 1,508 | 15,112 |
| `transformers/src/transformers/models/codegen/tokenization_codegen_fast.py` | 972 | 10,506 |
| `transformers/src/transformers/models/convbert/__init__.py` | 298 | 4,240 |
| `transformers/src/transformers/models/convbert/configuration_convbert.py` | 687 | 7,372 |
| `transformers/src/transformers/models/convbert/convert_convbert_original_tf1_checkpoint_to_pytorch_and_tf2.py` | 201 | 2,108 |
| `transformers/src/transformers/models/convbert/modeling_convbert.py` | 4,275 | 59,180 |
| `transformers/src/transformers/models/convbert/modeling_tf_convbert.py` | 4,112 | 55,146 |
| `transformers/src/transformers/models/convbert/tokenization_convbert.py` | 200 | 2,183 |
| `transformers/src/transformers/models/convbert/tokenization_convbert_fast.py` | 215 | 2,385 |
| `transformers/src/transformers/models/convnext/__init__.py` | 273 | 3,147 |
| `transformers/src/transformers/models/convnext/configuration_convnext.py` | 522 | 4,974 |
| `transformers/src/transformers/models/convnext/convert_convnext_to_pytorch.py` | 891 | 10,222 |
| `transformers/src/transformers/models/convnext/feature_extraction_convnext.py` | 805 | 7,318 |
| `transformers/src/transformers/models/convnext/modeling_convnext.py` | 1,684 | 18,952 |
| `transformers/src/transformers/models/convnext/modeling_tf_convnext.py` | 1,939 | 23,061 |
| `transformers/src/transformers/models/cpm/__init__.py` | 209 | 1,987 |
| `transformers/src/transformers/models/cpm/tokenization_cpm.py` | 618 | 5,544 |
| `transformers/src/transformers/models/cpm/tokenization_cpm_fast.py` | 628 | 5,873 |
| `transformers/src/transformers/models/ctrl/__init__.py` | 248 | 2,859 |
| `transformers/src/transformers/models/ctrl/configuration_ctrl.py` | 561 | 5,317 |
| `transformers/src/transformers/models/ctrl/modeling_ctrl.py` | 3,064 | 34,627 |
| `transformers/src/transformers/models/ctrl/modeling_tf_ctrl.py` | 2,967 | 34,335 |
| `transformers/src/transformers/models/ctrl/tokenization_ctrl.py` | 811 | 8,498 |
| `transformers/src/transformers/models/cvt/__init__.py` | 198 | 1,900 |
| `transformers/src/transformers/models/cvt/configuration_cvt.py` | 766 | 6,837 |
| `transformers/src/transformers/models/cvt/convert_cvt_original_pytorch_checkpoint_to_pytorch.py` | 697 | 13,550 |
| `transformers/src/transformers/models/cvt/modeling_cvt.py` | 2,273 | 28,879 |
| `transformers/src/transformers/models/data2vec/__init__.py` | 304 | 5,104 |
| `transformers/src/transformers/models/data2vec/configuration_data2vec_audio.py` | 1,613 | 16,222 |
| `transformers/src/transformers/models/data2vec/configuration_data2vec_text.py` | 697 | 7,231 |
| `transformers/src/transformers/models/data2vec/configuration_data2vec_vision.py` | 917 | 9,687 |
| `transformers/src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py` | 840 | 10,858 |
| `transformers/src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py` | 641 | 9,613 |
| `transformers/src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py` | 1,029 | 15,338 |
| `transformers/src/transformers/models/data2vec/modeling_data2vec_audio.py` | 5,205 | 66,560 |
| `transformers/src/transformers/models/data2vec/modeling_data2vec_text.py` | 5,687 | 72,198 |
| `transformers/src/transformers/models/data2vec/modeling_data2vec_vision.py` | 4,213 | 52,251 |
| `transformers/src/transformers/models/data2vec/modeling_tf_data2vec_vision.py` | 4,810 | 59,949 |
| `transformers/src/transformers/models/deberta/__init__.py` | 288 | 3,848 |
| `transformers/src/transformers/models/deberta/configuration_deberta.py` | 793 | 8,946 |
| `transformers/src/transformers/models/deberta/modeling_deberta.py` | 4,448 | 57,084 |
| `transformers/src/transformers/models/deberta/modeling_tf_deberta.py` | 4,717 | 62,054 |
| `transformers/src/transformers/models/deberta/tokenization_deberta.py` | 968 | 10,248 |
| `transformers/src/transformers/models/deberta/tokenization_deberta_fast.py` | 864 | 9,024 |
| `transformers/src/transformers/models/deberta_v2/__init__.py` | 292 | 4,070 |
| `transformers/src/transformers/models/deberta_v2/configuration_deberta_v2.py` | 786 | 8,711 |
| `transformers/src/transformers/models/deberta_v2/modeling_deberta_v2.py` | 5,056 | 66,337 |
| `transformers/src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py` | 5,071 | 68,347 |
| `transformers/src/transformers/models/deberta_v2/tokenization_deberta_v2.py` | 2,095 | 21,216 |
| `transformers/src/transformers/models/deberta_v2/tokenization_deberta_v2_fast.py` | 1,097 | 10,996 |
| `transformers/src/transformers/models/decision_transformer/__init__.py` | 214 | 2,332 |
| `transformers/src/transformers/models/decision_transformer/configuration_decision_transformer.py` | 775 | 7,902 |
| `transformers/src/transformers/models/decision_transformer/modeling_decision_transformer.py` | 3,664 | 43,748 |
| `transformers/src/transformers/models/deit/__init__.py` | 232 | 2,597 |
| `transformers/src/transformers/models/deit/configuration_deit.py` | 596 | 5,943 |
| `transformers/src/transformers/models/deit/convert_deit_timm_to_pytorch.py` | 727 | 9,219 |
| `transformers/src/transformers/models/deit/feature_extraction_deit.py` | 782 | 7,065 |
| `transformers/src/transformers/models/deit/modeling_deit.py` | 3,080 | 37,830 |
| `transformers/src/transformers/models/detr/__init__.py` | 228 | 2,438 |
| `transformers/src/transformers/models/detr/configuration_detr.py` | 972 | 10,031 |
| `transformers/src/transformers/models/detr/convert_detr_original_pytorch_checkpoint_to_pytorch.py` | 941 | 13,546 |
| `transformers/src/transformers/models/detr/feature_extraction_detr.py` | 4,213 | 42,282 |
| `transformers/src/transformers/models/detr/modeling_detr.py` | 9,734 | 108,250 |
| `transformers/src/transformers/models/dialogpt/__init__.py` | 0 | 0 |
| `transformers/src/transformers/models/dialogpt/convert_dialogpt_original_pytorch_checkpoint_to_pytorch.py` | 164 | 1,537 |
| `transformers/src/transformers/models/distilbert/__init__.py` | 342 | 5,338 |
| `transformers/src/transformers/models/distilbert/configuration_distilbert.py` | 646 | 6,955 |
| `transformers/src/transformers/models/distilbert/modeling_distilbert.py` | 4,196 | 50,244 |
| `transformers/src/transformers/models/distilbert/modeling_flax_distilbert.py` | 2,468 | 32,807 |
| `transformers/src/transformers/models/distilbert/modeling_tf_distilbert.py` | 3,692 | 46,637 |
| `transformers/src/transformers/models/distilbert/tokenization_distilbert.py` | 229 | 3,046 |
| `transformers/src/transformers/models/distilbert/tokenization_distilbert_fast.py` | 267 | 4,163 |
| `transformers/src/transformers/models/dit/__init__.py` | 0 | 0 |
| `transformers/src/transformers/models/dit/convert_dit_unilm_to_pytorch.py` | 694 | 9,341 |
| `transformers/src/transformers/models/dpr/__init__.py` | 314 | 4,706 |
| `transformers/src/transformers/models/dpr/configuration_dpr.py` | 625 | 6,787 |
| `transformers/src/transformers/models/dpr/convert_dpr_original_checkpoint_to_pytorch.py` | 495 | 6,097 |
| `transformers/src/transformers/models/dpr/modeling_dpr.py` | 2,550 | 28,751 |
| `transformers/src/transformers/models/dpr/modeling_tf_dpr.py` | 2,935 | 33,063 |
| `transformers/src/transformers/models/dpr/tokenization_dpr.py` | 1,730 | 19,824 |
| `transformers/src/transformers/models/dpr/tokenization_dpr_fast.py` | 1,758 | 20,210 |
| `transformers/src/transformers/models/dpt/__init__.py` | 232 | 2,485 |
| `transformers/src/transformers/models/dpt/configuration_dpt.py` | 854 | 8,415 |
| `transformers/src/transformers/models/dpt/convert_dpt_to_pytorch.py` | 1,003 | 11,785 |
| `transformers/src/transformers/models/dpt/feature_extraction_dpt.py` | 893 | 8,322 |
| `transformers/src/transformers/models/dpt/modeling_dpt.py` | 3,473 | 43,542 |
| `transformers/src/transformers/models/electra/__init__.py` | 348 | 5,428 |
| `transformers/src/transformers/models/electra/configuration_electra.py` | 941 | 9,904 |
| `transformers/src/transformers/models/electra/convert_electra_original_tf_checkpoint_to_pytorch.py` | 271 | 2,862 |
| `transformers/src/transformers/models/electra/modeling_electra.py` | 5,853 | 75,877 |
| `transformers/src/transformers/models/electra/modeling_flax_electra.py` | 4,387 | 60,541 |
| `transformers/src/transformers/models/electra/modeling_tf_electra.py` | 5,651 | 74,991 |
| `transformers/src/transformers/models/electra/tokenization_electra.py` | 225 | 2,991 |
| `transformers/src/transformers/models/electra/tokenization_electra_fast.py` | 267 | 4,161 |
| `transformers/src/transformers/models/encoder_decoder/__init__.py` | 244 | 2,622 |
| `transformers/src/transformers/models/encoder_decoder/configuration_encoder_decoder.py` | 479 | 4,840 |
| `transformers/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py` | 2,743 | 30,238 |
| `transformers/src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py` | 3,686 | 43,810 |
| `transformers/src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py` | 3,218 | 36,192 |
| `transformers/src/transformers/models/flaubert/__init__.py` | 262 | 3,587 |
| `transformers/src/transformers/models/flaubert/configuration_flaubert.py` | 1,051 | 9,307 |
| `transformers/src/transformers/models/flaubert/modeling_flaubert.py` | 1,787 | 18,489 |
| `transformers/src/transformers/models/flaubert/modeling_tf_flaubert.py` | 3,499 | 38,372 |
| `transformers/src/transformers/models/flaubert/tokenization_flaubert.py` | 490 | 5,796 |
| `transformers/src/transformers/models/flava/__init__.py` | 259 | 3,063 |
| `transformers/src/transformers/models/flava/configuration_flava.py` | 2,991 | 30,345 |
| `transformers/src/transformers/models/flava/convert_dalle_to_flava_codebook.py` | 326 | 3,428 |
| `transformers/src/transformers/models/flava/convert_flava_original_pytorch_to_hf.py` | 352 | 4,372 |
| `transformers/src/transformers/models/flava/feature_extraction_flava.py` | 1,599 | 16,508 |
| `transformers/src/transformers/models/flava/modeling_flava.py` | 7,533 | 96,549 |
| `transformers/src/transformers/models/flava/processing_flava.py` | 472 | 5,280 |
| `transformers/src/transformers/models/fnet/__init__.py` | 270 | 3,350 |
| `transformers/src/transformers/models/fnet/configuration_fnet.py` | 605 | 5,816 |
| `transformers/src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py` | 382 | 6,912 |
| `transformers/src/transformers/models/fnet/modeling_fnet.py` | 3,958 | 49,560 |
| `transformers/src/transformers/models/fnet/tokenization_fnet.py` | 1,320 | 13,234 |
| `transformers/src/transformers/models/fnet/tokenization_fnet_fast.py` | 883 | 8,557 |
| `transformers/src/transformers/models/fsmt/__init__.py` | 200 | 1,846 |
| `transformers/src/transformers/models/fsmt/configuration_fsmt.py` | 991 | 10,087 |
| `transformers/src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py` | 1,052 | 11,265 |
| `transformers/src/transformers/models/fsmt/modeling_fsmt.py` | 4,781 | 54,180 |
| `transformers/src/transformers/models/fsmt/tokenization_fsmt.py` | 1,988 | 20,153 |
| `transformers/src/transformers/models/funnel/__init__.py` | 302 | 4,297 |
| `transformers/src/transformers/models/funnel/configuration_funnel.py` | 898 | 9,484 |
| `transformers/src/transformers/models/funnel/convert_funnel_original_tf_checkpoint_to_pytorch.py` | 240 | 2,335 |
| `transformers/src/transformers/models/funnel/modeling_funnel.py` | 5,984 | 70,137 |
| `transformers/src/transformers/models/funnel/modeling_tf_funnel.py` | 6,021 | 74,261 |
| `transformers/src/transformers/models/funnel/tokenization_funnel.py` | 423 | 5,369 |
| `transformers/src/transformers/models/funnel/tokenization_funnel_fast.py` | 475 | 7,066 |
| `transformers/src/transformers/models/glpn/__init__.py` | 236 | 2,458 |
| `transformers/src/transformers/models/glpn/configuration_glpn.py` | 669 | 6,216 |
| `transformers/src/transformers/models/glpn/convert_glpn_to_pytorch.py` | 760 | 8,574 |
| `transformers/src/transformers/models/glpn/feature_extraction_glpn.py` | 645 | 5,939 |
| `transformers/src/transformers/models/glpn/modeling_glpn.py` | 2,483 | 31,458 |
| `transformers/src/transformers/models/gpt2/__init__.py` | 322 | 4,271 |
| `transformers/src/transformers/models/gpt2/configuration_gpt2.py` | 1,130 | 12,120 |
| `transformers/src/transformers/models/gpt2/convert_gpt2_original_tf_checkpoint_to_pytorch.py` | 249 | 2,532 |
| `transformers/src/transformers/models/gpt2/modeling_flax_gpt2.py` | 2,565 | 31,965 |
| `transformers/src/transformers/models/gpt2/modeling_gpt2.py` | 5,964 | 69,553 |
| `transformers/src/transformers/models/gpt2/modeling_tf_gpt2.py` | 5,061 | 57,493 |
| `transformers/src/transformers/models/gpt2/tokenization_gpt2.py` | 1,258 | 12,934 |
| `transformers/src/transformers/models/gpt2/tokenization_gpt2_fast.py` | 732 | 8,636 |
| `transformers/src/transformers/models/gpt_neo/__init__.py` | 240 | 2,729 |
| `transformers/src/transformers/models/gpt_neo/configuration_gpt_neo.py` | 1,075 | 11,801 |
| `transformers/src/transformers/models/gpt_neo/convert_gpt_neo_mesh_tf_to_pytorch.py` | 236 | 2,589 |
| `transformers/src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py` | 2,288 | 28,150 |
| `transformers/src/transformers/models/gpt_neo/modeling_gpt_neo.py` | 3,419 | 40,098 |
| `transformers/src/transformers/models/gpt_neox/__init__.py` | 231 | 2,512 |
| `transformers/src/transformers/models/gpt_neox/configuration_gpt_neox.py` | 595 | 5,919 |
| `transformers/src/transformers/models/gpt_neox/modeling_gpt_neox.py` | 2,653 | 28,872 |
| `transformers/src/transformers/models/gpt_neox/tokenization_gpt_neox_fast.py` | 557 | 5,788 |
| `transformers/src/transformers/models/gptj/__init__.py` | 282 | 3,451 |
| `transformers/src/transformers/models/gptj/configuration_gptj.py` | 871 | 9,220 |
| `transformers/src/transformers/models/gptj/modeling_flax_gptj.py` | 2,365 | 28,583 |
| `transformers/src/transformers/models/gptj/modeling_gptj.py` | 4,165 | 47,864 |
| `transformers/src/transformers/models/gptj/modeling_tf_gptj.py` | 4,015 | 46,431 |
| `transformers/src/transformers/models/herbert/__init__.py` | 186 | 1,643 |
| `transformers/src/transformers/models/herbert/tokenization_herbert.py` | 285 | 3,299 |
| `transformers/src/transformers/models/herbert/tokenization_herbert_fast.py` | 679 | 6,549 |
| `transformers/src/transformers/models/hubert/__init__.py` | 238 | 2,707 |
| `transformers/src/transformers/models/hubert/configuration_hubert.py` | 1,437 | 14,576 |
| `transformers/src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py` | 714 | 8,942 |
| `transformers/src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py` | 796 | 10,380 |
| `transformers/src/transformers/models/hubert/convert_hubert_original_s3prl_checkpoint_to_pytorch.py` | 238 | 2,895 |
| `transformers/src/transformers/models/hubert/modeling_hubert.py` | 4,498 | 57,711 |
| `transformers/src/transformers/models/hubert/modeling_tf_hubert.py` | 5,496 | 71,207 |
| `transformers/src/transformers/models/ibert/__init__.py` | 208 | 2,257 |
| `transformers/src/transformers/models/ibert/configuration_ibert.py` | 722 | 7,472 |
| `transformers/src/transformers/models/ibert/modeling_ibert.py` | 4,211 | 57,419 |
| `transformers/src/transformers/models/ibert/quant_modules.py` | 2,719 | 30,075 |
| `transformers/src/transformers/models/imagegpt/__init__.py` | 230 | 2,631 |
| `transformers/src/transformers/models/imagegpt/configuration_imagegpt.py` | 653 | 6,337 |
| `transformers/src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py` | 265 | 2,691 |
| `transformers/src/transformers/models/imagegpt/feature_extraction_imagegpt.py` | 802 | 7,194 |
| `transformers/src/transformers/models/imagegpt/modeling_imagegpt.py` | 4,669 | 54,392 |
| `transformers/src/transformers/models/layoutlm/__init__.py` | 286 | 3,790 |
| `transformers/src/transformers/models/layoutlm/configuration_layoutlm.py` | 802 | 8,327 |
| `transformers/src/transformers/models/layoutlm/modeling_layoutlm.py` | 4,128 | 54,274 |
| `transformers/src/transformers/models/layoutlm/modeling_tf_layoutlm.py` | 4,683 | 61,444 |
| `transformers/src/transformers/models/layoutlm/tokenization_layoutlm.py` | 200 | 2,076 |
| `transformers/src/transformers/models/layoutlm/tokenization_layoutlm_fast.py` | 220 | 2,585 |
| `transformers/src/transformers/models/layoutlmv2/__init__.py` | 276 | 3,500 |
| `transformers/src/transformers/models/layoutlmv2/configuration_layoutlmv2.py` | 953 | 11,224 |
| `transformers/src/transformers/models/layoutlmv2/feature_extraction_layoutlmv2.py` | 1,086 | 9,827 |
| `transformers/src/transformers/models/layoutlmv2/modeling_layoutlmv2.py` | 4,506 | 61,318 |
| `transformers/src/transformers/models/layoutlmv2/processing_layoutlmv2.py` | 748 | 7,815 |
| `transformers/src/transformers/models/layoutlmv2/tokenization_layoutlmv2.py` | 6,371 | 72,305 |
| `transformers/src/transformers/models/layoutlmv2/tokenization_layoutlmv2_fast.py` | 3,104 | 38,072 |
| `transformers/src/transformers/models/layoutlmv3/__init__.py` | 274 | 3,446 |
| `transformers/src/transformers/models/layoutlmv3/configuration_layoutlmv3.py` | 804 | 8,571 |
| `transformers/src/transformers/models/layoutlmv3/feature_extraction_layoutlmv3.py` | 1,157 | 10,636 |
| `transformers/src/transformers/models/layoutlmv3/modeling_layoutlmv3.py` | 4,095 | 54,989 |
| `transformers/src/transformers/models/layoutlmv3/processing_layoutlmv3.py` | 731 | 7,678 |
| `transformers/src/transformers/models/layoutlmv3/tokenization_layoutlmv3.py` | 6,474 | 72,804 |
| `transformers/src/transformers/models/layoutlmv3/tokenization_layoutlmv3_fast.py` | 3,198 | 40,180 |
| `transformers/src/transformers/models/layoutxlm/__init__.py` | 218 | 2,208 |
| `transformers/src/transformers/models/layoutxlm/processing_layoutxlm.py` | 729 | 7,608 |
| `transformers/src/transformers/models/layoutxlm/tokenization_layoutxlm.py` | 4,412 | 50,489 |
| `transformers/src/transformers/models/layoutxlm/tokenization_layoutxlm_fast.py` | 2,792 | 32,651 |
| `transformers/src/transformers/models/led/__init__.py` | 272 | 3,179 |
| `transformers/src/transformers/models/led/configuration_led.py` | 718 | 7,634 |
| `transformers/src/transformers/models/led/modeling_led.py` | 11,442 | 137,209 |
| `transformers/src/transformers/models/led/modeling_tf_led.py` | 9,206 | 114,757 |
| `transformers/src/transformers/models/led/tokenization_led.py` | 332 | 3,885 |
| `transformers/src/transformers/models/led/tokenization_led_fast.py` | 349 | 4,129 |
| `transformers/src/transformers/models/levit/__init__.py` | 228 | 2,505 |
| `transformers/src/transformers/models/levit/configuration_levit.py` | 600 | 5,326 |
| `transformers/src/transformers/models/levit/convert_levit_timm_to_pytorch.py` | 522 | 6,151 |
| `transformers/src/transformers/models/levit/feature_extraction_levit.py` | 722 | 6,697 |
| `transformers/src/transformers/models/levit/modeling_levit.py` | 2,275 | 29,602 |
| `transformers/src/transformers/models/longformer/__init__.py` | 300 | 4,367 |
| `transformers/src/transformers/models/longformer/configuration_longformer.py` | 355 | 3,494 |
| `transformers/src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py` | 257 | 3,027 |
| `transformers/src/transformers/models/longformer/modeling_longformer.py` | 9,827 | 112,544 |
| `transformers/src/transformers/models/longformer/modeling_tf_longformer.py` | 10,511 | 124,585 |
| `transformers/src/transformers/models/longformer/tokenization_longformer.py` | 216 | 3,314 |
| `transformers/src/transformers/models/longformer/tokenization_longformer_fast.py` | 261 | 4,462 |
| `transformers/src/transformers/models/longt5/__init__.py` | 240 | 2,717 |
| `transformers/src/transformers/models/longt5/configuration_longt5.py` | 803 | 8,481 |
| `transformers/src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py` | 600 | 11,088 |
| `transformers/src/transformers/models/longt5/modeling_flax_longt5.py` | 7,891 | 104,214 |
| `transformers/src/transformers/models/longt5/modeling_longt5.py` | 8,146 | 103,075 |
| `transformers/src/transformers/models/luke/__init__.py` | 212 | 2,250 |
| `transformers/src/transformers/models/luke/configuration_luke.py` | 623 | 6,358 |
| `transformers/src/transformers/models/luke/convert_luke_original_pytorch_checkpoint_to_pytorch.py` | 664 | 7,468 |
| `transformers/src/transformers/models/luke/modeling_luke.py` | 6,114 | 75,160 |
| `transformers/src/transformers/models/luke/tokenization_luke.py` | 5,514 | 69,505 |
| `transformers/src/transformers/models/lxmert/__init__.py` | 284 | 3,567 |
| `transformers/src/transformers/models/lxmert/configuration_lxmert.py` | 999 | 9,510 |
| `transformers/src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py` | 216 | 2,109 |
| `transformers/src/transformers/models/lxmert/modeling_lxmert.py` | 5,200 | 65,023 |
| `transformers/src/transformers/models/lxmert/modeling_tf_lxmert.py` | 4,767 | 62,819 |
| `transformers/src/transformers/models/lxmert/tokenization_lxmert.py` | 180 | 1,675 |
| `transformers/src/transformers/models/lxmert/tokenization_lxmert_fast.py` | 202 | 2,061 |
| `transformers/src/transformers/models/m2m_100/__init__.py` | 214 | 2,163 |
| `transformers/src/transformers/models/m2m_100/configuration_m2m_100.py` | 1,166 | 13,561 |
| `transformers/src/transformers/models/m2m_100/convert_m2m100_original_checkpoint_to_pytorch.py` | 235 | 3,118 |
| `transformers/src/transformers/models/m2m_100/modeling_m2m_100.py` | 5,268 | 64,635 |
| `transformers/src/transformers/models/m2m_100/tokenization_m2m_100.py` | 1,597 | 17,039 |
| `transformers/src/transformers/models/marian/__init__.py` | 299 | 3,615 |
| `transformers/src/transformers/models/marian/configuration_marian.py` | 1,516 | 18,678 |
| `transformers/src/transformers/models/marian/convert_marian_tatoeba_to_pytorch.py` | 2,597 | 36,254 |
| `transformers/src/transformers/models/marian/convert_marian_to_pytorch.py` | 2,046 | 26,746 |
| `transformers/src/transformers/models/marian/modeling_flax_marian.py` | 4,888 | 64,294 |
| `transformers/src/transformers/models/marian/modeling_marian.py` | 6,787 | 82,322 |
| `transformers/src/transformers/models/marian/modeling_tf_marian.py` | 5,560 | 67,868 |
| `transformers/src/transformers/models/marian/tokenization_marian.py` | 1,526 | 17,377 |
| `transformers/src/transformers/models/maskformer/__init__.py` | 225 | 2,484 |
| `transformers/src/transformers/models/maskformer/configuration_maskformer.py` | 810 | 8,864 |
| `transformers/src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py` | 1,779 | 32,240 |
| `transformers/src/transformers/models/maskformer/feature_extraction_maskformer.py` | 3,225 | 32,357 |
| `transformers/src/transformers/models/maskformer/modeling_maskformer.py` | 10,746 | 122,352 |
| `transformers/src/transformers/models/mbart/__init__.py` | 338 | 4,574 |
| `transformers/src/transformers/models/mbart/configuration_mbart.py` | 1,492 | 18,366 |
| `transformers/src/transformers/models/mbart/convert_mbart_original_checkpoint_to_pytorch.py` | 260 | 3,035 |
| `transformers/src/transformers/models/mbart/modeling_flax_mbart.py` | 5,595 | 75,152 |
| `transformers/src/transformers/models/mbart/modeling_mbart.py` | 7,170 | 88,745 |
| `transformers/src/transformers/models/mbart/modeling_tf_mbart.py` | 5,741 | 68,827 |
| `transformers/src/transformers/models/mbart/tokenization_mbart.py` | 1,446 | 15,084 |
| `transformers/src/transformers/models/mbart/tokenization_mbart_fast.py` | 1,076 | 12,286 |
| `transformers/src/transformers/models/mbart50/__init__.py` | 209 | 2,018 |
| `transformers/src/transformers/models/mbart50/tokenization_mbart50.py` | 1,653 | 16,396 |
| `transformers/src/transformers/models/mbart50/tokenization_mbart50_fast.py` | 1,162 | 12,544 |
| `transformers/src/transformers/models/mctct/__init__.py` | 232 | 2,413 |
| `transformers/src/transformers/models/mctct/configuration_mctct.py` | 923 | 9,283 |
| `transformers/src/transformers/models/mctct/feature_extraction_mctct.py` | 1,522 | 15,806 |
| `transformers/src/transformers/models/mctct/modeling_mctct.py` | 2,726 | 33,612 |
| `transformers/src/transformers/models/mctct/processing_mctct.py` | 393 | 3,653 |
| `transformers/src/transformers/models/megatron_bert/__init__.py` | 217 | 2,677 |
| `transformers/src/transformers/models/megatron_bert/configuration_megatron_bert.py` | 637 | 6,384 |
| `transformers/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py` | 1,277 | 13,689 |
| `transformers/src/transformers/models/megatron_bert/modeling_megatron_bert.py` | 6,612 | 83,434 |
| `transformers/src/transformers/models/megatron_gpt2/__init__.py` | 133 | 801 |
| `transformers/src/transformers/models/megatron_gpt2/convert_megatron_gpt2_checkpoint.py` | 1,248 | 13,632 |
| `transformers/src/transformers/models/mluke/__init__.py` | 181 | 1,527 |
| `transformers/src/transformers/models/mluke/convert_mluke_original_pytorch_checkpoint_to_pytorch.py` | 803 | 10,186 |
| `transformers/src/transformers/models/mluke/tokenization_mluke.py` | 6,698 | 81,221 |
| `transformers/src/transformers/models/mmbt/__init__.py` | 190 | 1,650 |
| `transformers/src/transformers/models/mmbt/configuration_mmbt.py` | 207 | 1,605 |
| `transformers/src/transformers/models/mmbt/modeling_mmbt.py` | 1,662 | 18,887 |
| `transformers/src/transformers/models/mobilebert/__init__.py` | 310 | 4,775 |
| `transformers/src/transformers/models/mobilebert/configuration_mobilebert.py` | 795 | 8,563 |
| `transformers/src/transformers/models/mobilebert/convert_mobilebert_original_tf_checkpoint_to_pytorch.py` | 219 | 2,200 |
| `transformers/src/transformers/models/mobilebert/modeling_mobilebert.py` | 5,579 | 70,784 |
| `transformers/src/transformers/models/mobilebert/modeling_tf_mobilebert.py` | 5,556 | 73,714 |
| `transformers/src/transformers/models/mobilebert/tokenization_mobilebert.py` | 179 | 1,669 |
| `transformers/src/transformers/models/mobilebert/tokenization_mobilebert_fast.py` | 199 | 2,033 |
| `transformers/src/transformers/models/mpnet/__init__.py` | 297 | 4,046 |
| `transformers/src/transformers/models/mpnet/configuration_mpnet.py` | 553 | 5,442 |
| `transformers/src/transformers/models/mpnet/modeling_mpnet.py` | 3,361 | 43,207 |
| `transformers/src/transformers/models/mpnet/modeling_tf_mpnet.py` | 3,832 | 50,220 |
| `transformers/src/transformers/models/mpnet/tokenization_mpnet.py` | 2,193 | 22,023 |
| `transformers/src/transformers/models/mpnet/tokenization_mpnet_fast.py` | 927 | 8,930 |
| `transformers/src/transformers/models/mt5/__init__.py` | 290 | 3,278 |
| `transformers/src/transformers/models/mt5/configuration_mt5.py` | 633 | 6,304 |
| `transformers/src/transformers/models/mt5/modeling_flax_mt5.py` | 344 | 3,371 |
| `transformers/src/transformers/models/mt5/modeling_mt5.py` | 397 | 4,113 |
| `transformers/src/transformers/models/mt5/modeling_tf_mt5.py` | 364 | 3,500 |
| `transformers/src/transformers/models/nezha/__init__.py` | 221 | 2,441 |
| `transformers/src/transformers/models/nezha/configuration_nezha.py` | 455 | 5,039 |
| `transformers/src/transformers/models/nezha/modeling_nezha.py` | 5,963 | 75,718 |
| `transformers/src/transformers/models/nystromformer/__init__.py` | 219 | 2,545 |
| `transformers/src/transformers/models/nystromformer/configuration_nystromformer.py` | 644 | 6,622 |
| `transformers/src/transformers/models/nystromformer/convert_nystromformer_original_pytorch_checkpoint_to_pytorch.py` | 372 | 4,198 |
| `transformers/src/transformers/models/nystromformer/modeling_nystromformer.py` | 3,727 | 49,379 |
| `transformers/src/transformers/models/openai/__init__.py` | 286 | 3,829 |
| `transformers/src/transformers/models/openai/configuration_openai.py` | 795 | 7,587 |
| `transformers/src/transformers/models/openai/convert_openai_original_tf_checkpoint_to_pytorch.py` | 251 | 2,666 |
| `transformers/src/transformers/models/openai/modeling_openai.py` | 3,452 | 37,926 |
| `transformers/src/transformers/models/openai/modeling_tf_openai.py` | 3,458 | 38,780 |
| `transformers/src/transformers/models/openai/tokenization_openai.py` | 837 | 8,464 |
| `transformers/src/transformers/models/openai/tokenization_openai_fast.py` | 310 | 3,046 |
| `transformers/src/transformers/models/opt/__init__.py` | 265 | 2,933 |
| `transformers/src/transformers/models/opt/configuration_opt.py` | 657 | 6,878 |
| `transformers/src/transformers/models/opt/convert_opt_original_pytorch_checkpoint_to_pytorch.py` | 282 | 3,018 |
| `transformers/src/transformers/models/opt/modeling_flax_opt.py` | 2,558 | 31,652 |
| `transformers/src/transformers/models/opt/modeling_opt.py` | 3,919 | 44,658 |
| `transformers/src/transformers/models/opt/modeling_tf_opt.py` | 4,113 | 46,726 |
| `transformers/src/transformers/models/pegasus/__init__.py` | 328 | 4,282 |
| `transformers/src/transformers/models/pegasus/configuration_pegasus.py` | 753 | 7,870 |
| `transformers/src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py` | 499 | 5,362 |
| `transformers/src/transformers/models/pegasus/modeling_flax_pegasus.py` | 4,965 | 66,082 |
| `transformers/src/transformers/models/pegasus/modeling_pegasus.py` | 6,725 | 81,230 |
| `transformers/src/transformers/models/pegasus/modeling_tf_pegasus.py` | 5,555 | 67,718 |
| `transformers/src/transformers/models/pegasus/tokenization_pegasus.py` | 1,271 | 13,288 |
| `transformers/src/transformers/models/pegasus/tokenization_pegasus_fast.py` | 938 | 9,936 |
| `transformers/src/transformers/models/perceiver/__init__.py` | 253 | 3,310 |
| `transformers/src/transformers/models/perceiver/configuration_perceiver.py` | 1,145 | 12,132 |
| `transformers/src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py` | 1,630 | 21,260 |
| `transformers/src/transformers/models/perceiver/feature_extraction_perceiver.py` | 892 | 8,189 |
| `transformers/src/transformers/models/perceiver/modeling_perceiver.py` | 11,883 | 145,246 |
| `transformers/src/transformers/models/perceiver/tokenization_perceiver.py` | 896 | 8,945 |
| `transformers/src/transformers/models/phobert/__init__.py` | 157 | 1,126 |
| `transformers/src/transformers/models/phobert/tokenization_phobert.py` | 1,369 | 13,557 |
| `transformers/src/transformers/models/plbart/__init__.py` | 232 | 2,600 |
| `transformers/src/transformers/models/plbart/configuration_plbart.py` | 824 | 8,697 |
| `transformers/src/transformers/models/plbart/convert_plbart_original_checkpoint_to_torch.py` | 272 | 3,553 |
| `transformers/src/transformers/models/plbart/modeling_plbart.py` | 6,689 | 82,063 |
| `transformers/src/transformers/models/plbart/tokenization_plbart.py` | 1,884 | 20,964 |
| `transformers/src/transformers/models/poolformer/__init__.py` | 233 | 2,520 |
| `transformers/src/transformers/models/poolformer/configuration_poolformer.py` | 578 | 5,248 |
| `transformers/src/transformers/models/poolformer/convert_poolformer_original_to_pytorch.py` | 773 | 7,961 |
| `transformers/src/transformers/models/poolformer/feature_extraction_poolformer.py` | 799 | 7,478 |
| `transformers/src/transformers/models/poolformer/modeling_poolformer.py` | 1,477 | 18,213 |
| `transformers/src/transformers/models/prophetnet/__init__.py` | 212 | 2,328 |
| `transformers/src/transformers/models/prophetnet/configuration_prophetnet.py` | 913 | 9,061 |
| `transformers/src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py` | 527 | 7,055 |
| `transformers/src/transformers/models/prophetnet/modeling_prophetnet.py` | 9,141 | 113,831 |
| `transformers/src/transformers/models/prophetnet/tokenization_prophetnet.py` | 1,274 | 12,761 |
| `transformers/src/transformers/models/qdqbert/__init__.py` | 217 | 2,573 |
| `transformers/src/transformers/models/qdqbert/configuration_qdqbert.py` | 585 | 5,762 |
| `transformers/src/transformers/models/qdqbert/modeling_qdqbert.py` | 6,079 | 77,667 |
| `transformers/src/transformers/models/rag/__init__.py` | 246 | 2,597 |
| `transformers/src/transformers/models/rag/configuration_rag.py` | 813 | 8,804 |
| `transformers/src/transformers/models/rag/modeling_rag.py` | 7,686 | 91,744 |
| `transformers/src/transformers/models/rag/modeling_tf_rag.py` | 7,548 | 89,988 |
| `transformers/src/transformers/models/rag/retrieval_rag.py` | 2,422 | 28,664 |
| `transformers/src/transformers/models/rag/tokenization_rag.py` | 411 | 4,898 |
| `transformers/src/transformers/models/realm/__init__.py` | 249 | 2,846 |
| `transformers/src/transformers/models/realm/configuration_realm.py` | 774 | 8,913 |
| `transformers/src/transformers/models/realm/modeling_realm.py` | 6,216 | 82,695 |
| `transformers/src/transformers/models/realm/retrieval_realm.py` | 512 | 6,380 |
| `transformers/src/transformers/models/realm/tokenization_realm.py` | 2,388 | 25,484 |
| `transformers/src/transformers/models/realm/tokenization_realm_fast.py` | 1,217 | 14,580 |
| `transformers/src/transformers/models/reformer/__init__.py` | 266 | 3,310 |
| `transformers/src/transformers/models/reformer/configuration_reformer.py` | 1,361 | 13,440 |
| `transformers/src/transformers/models/reformer/convert_reformer_trax_checkpoint_to_pytorch.py` | 575 | 7,818 |
| `transformers/src/transformers/models/reformer/modeling_reformer.py` | 9,170 | 116,600 |
| `transformers/src/transformers/models/reformer/tokenization_reformer.py` | 644 | 6,894 |
| `transformers/src/transformers/models/reformer/tokenization_reformer_fast.py` | 446 | 4,824 |
| `transformers/src/transformers/models/regnet/__init__.py` | 208 | 1,988 |
| `transformers/src/transformers/models/regnet/configuration_regnet.py` | 469 | 4,087 |
| `transformers/src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py` | 1,086 | 11,781 |
| `transformers/src/transformers/models/regnet/convert_regnet_to_pytorch.py` | 1,512 | 18,726 |
| `transformers/src/transformers/models/regnet/modeling_regnet.py` | 1,453 | 17,638 |
| `transformers/src/transformers/models/rembert/__init__.py` | 320 | 4,639 |
| `transformers/src/transformers/models/rembert/configuration_rembert.py` | 659 | 6,643 |
| `transformers/src/transformers/models/rembert/convert_rembert_tf_checkpoint_to_pytorch.py` | 220 | 2,208 |
| `transformers/src/transformers/models/rembert/modeling_rembert.py` | 5,433 | 68,289 |
| `transformers/src/transformers/models/rembert/modeling_tf_rembert.py` | 5,766 | 75,769 |
| `transformers/src/transformers/models/rembert/tokenization_rembert.py` | 1,113 | 10,491 |
| `transformers/src/transformers/models/rembert/tokenization_rembert_fast.py` | 1,130 | 10,432 |
| `transformers/src/transformers/models/resnet/__init__.py` | 209 | 2,007 |
| `transformers/src/transformers/models/resnet/configuration_resnet.py` | 480 | 4,441 |
| `transformers/src/transformers/models/resnet/convert_resnet_to_pytorch.py` | 663 | 7,298 |
| `transformers/src/transformers/models/resnet/modeling_resnet.py` | 1,395 | 16,282 |
| `transformers/src/transformers/models/retribert/__init__.py` | 232 | 2,521 |
| `transformers/src/transformers/models/retribert/configuration_retribert.py` | 547 | 5,404 |
| `transformers/src/transformers/models/retribert/modeling_retribert.py` | 816 | 9,469 |
| `transformers/src/transformers/models/retribert/tokenization_retribert.py` | 190 | 1,847 |
| `transformers/src/transformers/models/retribert/tokenization_retribert_fast.py` | 212 | 2,251 |
| `transformers/src/transformers/models/roberta/__init__.py` | 344 | 5,262 |
| `transformers/src/transformers/models/roberta/configuration_roberta.py` | 344 | 3,465 |
| `transformers/src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py` | 542 | 8,002 |
| `transformers/src/transformers/models/roberta/modeling_flax_roberta.py` | 3,917 | 55,024 |
| `transformers/src/transformers/models/roberta/modeling_roberta.py` | 5,665 | 71,680 |
| `transformers/src/transformers/models/roberta/modeling_tf_roberta.py` | 6,109 | 78,872 |
| `transformers/src/transformers/models/roberta/tokenization_roberta.py` | 1,833 | 17,956 |
| `transformers/src/transformers/models/roberta/tokenization_roberta_fast.py` | 1,243 | 13,674 |
| `transformers/src/transformers/models/roformer/__init__.py` | 348 | 5,504 |
| `transformers/src/transformers/models/roformer/configuration_roformer.py` | 703 | 7,544 |
| `transformers/src/transformers/models/roformer/convert_roformer_original_tf_checkpoint_to_pytorch.py` | 224 | 2,240 |
| `transformers/src/transformers/models/roformer/modeling_flax_roformer.py` | 2,851 | 39,631 |
| `transformers/src/transformers/models/roformer/modeling_roformer.py` | 5,254 | 67,169 |
| `transformers/src/transformers/models/roformer/modeling_tf_roformer.py` | 4,621 | 61,338 |
| `transformers/src/transformers/models/roformer/tokenization_roformer.py` | 1,310 | 14,353 |
| `transformers/src/transformers/models/roformer/tokenization_roformer_fast.py` | 670 | 8,277 |
| `transformers/src/transformers/models/roformer/tokenization_utils.py` | 258 | 2,652 |
| `transformers/src/transformers/models/segformer/__init__.py` | 232 | 2,693 |
| `transformers/src/transformers/models/segformer/configuration_segformer.py` | 724 | 7,065 |
| `transformers/src/transformers/models/segformer/convert_segformer_original_to_pytorch.py` | 1,454 | 17,096 |
| `transformers/src/transformers/models/segformer/feature_extraction_segformer.py` | 973 | 9,498 |
| `transformers/src/transformers/models/segformer/modeling_segformer.py` | 2,780 | 35,213 |
| `transformers/src/transformers/models/sew/__init__.py` | 200 | 1,949 |
| `transformers/src/transformers/models/sew/configuration_sew.py` | 1,413 | 14,033 |
| `transformers/src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py` | 972 | 12,744 |
| `transformers/src/transformers/models/sew/modeling_sew.py` | 4,132 | 52,371 |
| `transformers/src/transformers/models/sew_d/__init__.py` | 200 | 1,975 |
| `transformers/src/transformers/models/sew_d/configuration_sew_d.py` | 1,614 | 16,270 |
| `transformers/src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py` | 1,004 | 13,574 |
| `transformers/src/transformers/models/sew_d/modeling_sew_d.py` | 5,497 | 71,788 |
| `transformers/src/transformers/models/speech_encoder_decoder/__init__.py` | 214 | 2,208 |
| `transformers/src/transformers/models/speech_encoder_decoder/configuration_speech_encoder_decoder.py` | 497 | 5,087 |
| `transformers/src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py` | 1,090 | 14,760 |
| `transformers/src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py` | 911 | 11,984 |
| `transformers/src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py` | 3,774 | 45,066 |
| `transformers/src/transformers/models/speech_encoder_decoder/modeling_speech_encoder_decoder.py` | 2,977 | 32,479 |
| `transformers/src/transformers/models/speech_to_text/__init__.py` | 307 | 4,127 |
| `transformers/src/transformers/models/speech_to_text/configuration_speech_to_text.py` | 891 | 9,489 |
| `transformers/src/transformers/models/speech_to_text/convert_s2t_fairseq_to_tfms.py` | 320 | 4,509 |
| `transformers/src/transformers/models/speech_to_text/feature_extraction_speech_to_text.py` | 1,143 | 11,512 |
| `transformers/src/transformers/models/speech_to_text/modeling_speech_to_text.py` | 5,315 | 65,592 |
| `transformers/src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py` | 5,607 | 69,598 |
| `transformers/src/transformers/models/speech_to_text/processing_speech_to_text.py` | 335 | 3,273 |
| `transformers/src/transformers/models/speech_to_text/tokenization_speech_to_text.py` | 1,037 | 11,148 |
| `transformers/src/transformers/models/speech_to_text_2/__init__.py` | 214 | 2,337 |
| `transformers/src/transformers/models/speech_to_text_2/configuration_speech_to_text_2.py` | 644 | 6,723 |
| `transformers/src/transformers/models/speech_to_text_2/modeling_speech_to_text_2.py` | 3,844 | 45,291 |
| `transformers/src/transformers/models/speech_to_text_2/processing_speech_to_text_2.py` | 335 | 3,245 |
| `transformers/src/transformers/models/speech_to_text_2/tokenization_speech_to_text_2.py` | 868 | 9,217 |
| `transformers/src/transformers/models/splinter/__init__.py` | 238 | 2,703 |
| `transformers/src/transformers/models/splinter/configuration_splinter.py` | 599 | 6,119 |
| `transformers/src/transformers/models/splinter/modeling_splinter.py` | 4,310 | 53,451 |
| `transformers/src/transformers/models/splinter/tokenization_splinter.py` | 2,141 | 22,015 |
| `transformers/src/transformers/models/splinter/tokenization_splinter_fast.py` | 932 | 9,658 |
| `transformers/src/transformers/models/squeezebert/__init__.py` | 250 | 3,167 |
| `transformers/src/transformers/models/squeezebert/configuration_squeezebert.py` | 760 | 7,887 |
| `transformers/src/transformers/models/squeezebert/modeling_squeezebert.py` | 3,767 | 45,321 |
| `transformers/src/transformers/models/squeezebert/tokenization_squeezebert.py` | 206 | 2,325 |
| `transformers/src/transformers/models/squeezebert/tokenization_squeezebert_fast.py` | 236 | 3,048 |
| `transformers/src/transformers/models/swin/__init__.py` | 248 | 2,827 |
| `transformers/src/transformers/models/swin/configuration_swin.py` | 665 | 6,448 |
| `transformers/src/transformers/models/swin/convert_swin_timm_to_pytorch.py` | 464 | 5,805 |
| `transformers/src/transformers/models/swin/modeling_swin.py` | 4,535 | 53,927 |
| `transformers/src/transformers/models/swin/modeling_tf_swin.py` | 5,445 | 63,729 |
| `transformers/src/transformers/models/t5/__init__.py` | 336 | 4,328 |
| `transformers/src/transformers/models/t5/configuration_t5.py` | 721 | 7,430 |
| `transformers/src/transformers/models/t5/convert_t5_original_tf_checkpoint_to_pytorch.py` | 219 | 2,120 |
| `transformers/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py` | 524 | 10,537 |
| `transformers/src/transformers/models/t5/download_from_gcp.sh` | 149 | 1,591 |
| `transformers/src/transformers/models/t5/modeling_flax_t5.py` | 5,227 | 69,071 |
| `transformers/src/transformers/models/t5/modeling_t5.py` | 6,564 | 82,765 |
| `transformers/src/transformers/models/t5/modeling_tf_t5.py` | 6,249 | 77,562 |
| `transformers/src/transformers/models/t5/tokenization_t5.py` | 1,415 | 14,875 |
| `transformers/src/transformers/models/t5/tokenization_t5_fast.py` | 972 | 10,476 |
| `transformers/src/transformers/models/tapas/__init__.py` | 254 | 3,123 |
| `transformers/src/transformers/models/tapas/configuration_tapas.py` | 1,152 | 12,900 |
| `transformers/src/transformers/models/tapas/convert_tapas_original_tf_checkpoint_to_pytorch.py` | 451 | 5,049 |
| `transformers/src/transformers/models/tapas/modeling_tapas.py` | 9,640 | 110,426 |
| `transformers/src/transformers/models/tapas/modeling_tf_tapas.py` | 8,965 | 106,879 |
| `transformers/src/transformers/models/tapas/tokenization_tapas.py` | 10,662 | 120,555 |
| `transformers/src/transformers/models/tapex/__init__.py` | 164 | 1,138 |
| `transformers/src/transformers/models/tapex/tokenization_tapex.py` | 5,597 | 65,960 |
| `transformers/src/transformers/models/trajectory_transformer/__init__.py` | 212 | 2,284 |
| `transformers/src/transformers/models/trajectory_transformer/configuration_trajectory_transformer.py` | 751 | 7,848 |
| `transformers/src/transformers/models/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py` | 241 | 3,139 |
| `transformers/src/transformers/models/trajectory_transformer/modeling_trajectory_transformer.py` | 2,230 | 26,062 |
| `transformers/src/transformers/models/transfo_xl/__init__.py` | 258 | 3,353 |
| `transformers/src/transformers/models/transfo_xl/configuration_transfo_xl.py` | 826 | 7,872 |
| `transformers/src/transformers/models/transfo_xl/convert_transfo_xl_original_tf_checkpoint_to_pytorch.py` | 416 | 4,916 |
| `transformers/src/transformers/models/transfo_xl/modeling_tf_transfo_xl.py` | 4,119 | 46,199 |
| `transformers/src/transformers/models/transfo_xl/modeling_tf_transfo_xl_utilities.py` | 609 | 7,597 |
| `transformers/src/transformers/models/transfo_xl/modeling_transfo_xl.py` | 5,003 | 55,872 |
| `transformers/src/transformers/models/transfo_xl/modeling_transfo_xl_utilities.py` | 907 | 10,675 |
| `transformers/src/transformers/models/transfo_xl/tokenization_transfo_xl.py` | 2,815 | 30,515 |
| `transformers/src/transformers/models/trocr/__init__.py` | 206 | 1,989 |
| `transformers/src/transformers/models/trocr/configuration_trocr.py` | 671 | 6,955 |
| `transformers/src/transformers/models/trocr/modeling_trocr.py` | 4,012 | 46,820 |
| `transformers/src/transformers/models/trocr/processing_trocr.py` | 334 | 3,239 |
| `transformers/src/transformers/models/unispeech/__init__.py` | 206 | 2,189 |
| `transformers/src/transformers/models/unispeech/configuration_unispeech.py` | 1,629 | 16,955 |
| `transformers/src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py` | 870 | 11,340 |
| `transformers/src/transformers/models/unispeech/modeling_unispeech.py` | 5,413 | 70,045 |
| `transformers/src/transformers/models/unispeech_sat/__init__.py` | 212 | 2,438 |
| `transformers/src/transformers/models/unispeech_sat/configuration_unispeech_sat.py` | 1,797 | 18,400 |
| `transformers/src/transformers/models/unispeech_sat/convert_unispeech_original_s3prl_checkpoint_to_pytorch.py` | 327 | 4,870 |
| `transformers/src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py` | 726 | 9,289 |
| `transformers/src/transformers/models/unispeech_sat/modeling_unispeech_sat.py` | 6,374 | 83,608 |
| `transformers/src/transformers/models/van/__init__.py` | 206 | 1,935 |
| `transformers/src/transformers/models/van/configuration_van.py` | 524 | 4,834 |
| `transformers/src/transformers/models/van/convert_van_to_pytorch.py` | 842 | 10,374 |
| `transformers/src/transformers/models/van/modeling_van.py` | 1,828 | 21,665 |
| `transformers/src/transformers/models/vilt/__init__.py` | 248 | 2,784 |
| `transformers/src/transformers/models/vilt/configuration_vilt.py` | 715 | 6,962 |
| `transformers/src/transformers/models/vilt/convert_vilt_original_to_pytorch.py` | 913 | 12,866 |
| `transformers/src/transformers/models/vilt/feature_extraction_vilt.py` | 1,323 | 12,399 |
| `transformers/src/transformers/models/vilt/modeling_vilt.py` | 4,966 | 59,350 |
| `transformers/src/transformers/models/vilt/processing_vilt.py` | 409 | 4,535 |
| `transformers/src/transformers/models/vision_encoder_decoder/__init__.py` | 244 | 2,726 |
| `transformers/src/transformers/models/vision_encoder_decoder/configuration_vision_encoder_decoder.py` | 496 | 5,073 |
| `transformers/src/transformers/models/vision_encoder_decoder/convert_trocr_unilm_to_pytorch.py` | 767 | 10,163 |
| `transformers/src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py` | 3,487 | 41,687 |
| `transformers/src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py` | 3,297 | 37,964 |
| `transformers/src/transformers/models/vision_encoder_decoder/modeling_vision_encoder_decoder.py` | 2,570 | 28,620 |
| `transformers/src/transformers/models/vision_text_dual_encoder/__init__.py` | 229 | 2,410 |
| `transformers/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py` | 490 | 5,277 |
| `transformers/src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py` | 2,324 | 26,699 |
| `transformers/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py` | 2,253 | 25,072 |
| `transformers/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py` | 607 | 5,496 |
| `transformers/src/transformers/models/visual_bert/__init__.py` | 208 | 2,406 |
| `transformers/src/transformers/models/visual_bert/configuration_visual_bert.py` | 720 | 7,911 |
| `transformers/src/transformers/models/visual_bert/convert_visual_bert_original_pytorch_checkpoint_to_pytorch.py` | 437 | 5,158 |
| `transformers/src/transformers/models/visual_bert/modeling_visual_bert.py` | 5,206 | 69,685 |
| `transformers/src/transformers/models/vit/__init__.py` | 300 | 3,639 |
| `transformers/src/transformers/models/vit/configuration_vit.py` | 592 | 5,819 |
| `transformers/src/transformers/models/vit/convert_dino_to_pytorch.py` | 714 | 8,856 |
| `transformers/src/transformers/models/vit/convert_vit_timm_to_pytorch.py` | 796 | 10,194 |
| `transformers/src/transformers/models/vit/feature_extraction_vit.py` | 695 | 6,307 |
| `transformers/src/transformers/models/vit/modeling_flax_vit.py` | 1,887 | 24,409 |
| `transformers/src/transformers/models/vit/modeling_tf_vit.py` | 2,599 | 32,280 |
| `transformers/src/transformers/models/vit/modeling_vit.py` | 2,719 | 33,664 |
| `transformers/src/transformers/models/vit_mae/__init__.py` | 237 | 2,599 |
| `transformers/src/transformers/models/vit_mae/configuration_vit_mae.py` | 656 | 6,579 |
| `transformers/src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py` | 601 | 7,532 |
| `transformers/src/transformers/models/vit_mae/modeling_tf_vit_mae.py` | 3,956 | 47,031 |
| `transformers/src/transformers/models/vit_mae/modeling_vit_mae.py` | 3,585 | 42,862 |
| `transformers/src/transformers/models/wav2vec2/__init__.py` | 308 | 4,214 |
| `transformers/src/transformers/models/wav2vec2/configuration_wav2vec2.py` | 1,933 | 19,582 |
| `transformers/src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py` | 833 | 11,080 |
| `transformers/src/transformers/models/wav2vec2/convert_wav2vec2_original_s3prl_checkpoint_to_pytorch.py` | 327 | 4,838 |
| `transformers/src/transformers/models/wav2vec2/feature_extraction_wav2vec2.py` | 1,072 | 11,225 |
| `transformers/src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py` | 4,437 | 57,357 |
| `transformers/src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py` | 5,601 | 71,916 |
| `transformers/src/transformers/models/wav2vec2/modeling_wav2vec2.py` | 7,159 | 92,085 |
| `transformers/src/transformers/models/wav2vec2/processing_wav2vec2.py` | 472 | 4,877 |
| `transformers/src/transformers/models/wav2vec2/tokenization_wav2vec2.py` | 3,590 | 39,089 |
| `transformers/src/transformers/models/wav2vec2_conformer/__init__.py` | 212 | 2,546 |
| `transformers/src/transformers/models/wav2vec2_conformer/configuration_wav2vec2_conformer.py` | 1,996 | 20,705 |
| `transformers/src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py` | 941 | 13,256 |
| `transformers/src/transformers/models/wav2vec2_conformer/modeling_wav2vec2_conformer.py` | 7,145 | 95,764 |
| `transformers/src/transformers/models/wav2vec2_phoneme/__init__.py` | 157 | 1,164 |
| `transformers/src/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py` | 2,363 | 25,933 |
| `transformers/src/transformers/models/wav2vec2_with_lm/__init__.py` | 157 | 1,152 |
| `transformers/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py` | 2,012 | 22,525 |
| `transformers/src/transformers/models/wavlm/__init__.py` | 204 | 2,130 |
| `transformers/src/transformers/models/wavlm/configuration_wavlm.py` | 1,864 | 18,818 |
| `transformers/src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py` | 688 | 8,581 |
| `transformers/src/transformers/models/wavlm/convert_wavlm_original_s3prl_checkpoint_to_pytorch.py` | 327 | 4,814 |
| `transformers/src/transformers/models/wavlm/modeling_wavlm.py` | 5,921 | 77,726 |
| `transformers/src/transformers/models/xglm/__init__.py` | 295 | 3,381 |
| `transformers/src/transformers/models/xglm/configuration_xglm.py` | 616 | 6,055 |
| `transformers/src/transformers/models/xglm/convert_xglm_original_ckpt_to_trfms.py` | 141 | 2,325 |
| `transformers/src/transformers/models/xglm/modeling_flax_xglm.py` | 2,678 | 33,709 |
| `transformers/src/transformers/models/xglm/modeling_xglm.py` | 3,851 | 44,984 |
| `transformers/src/transformers/models/xglm/tokenization_xglm.py` | 1,396 | 13,276 |
| `transformers/src/transformers/models/xglm/tokenization_xglm_fast.py` | 824 | 8,032 |
| `transformers/src/transformers/models/xlm/__init__.py` | 266 | 3,463 |
| `transformers/src/transformers/models/xlm/configuration_xlm.py` | 1,187 | 11,952 |
| `transformers/src/transformers/models/xlm/convert_xlm_original_pytorch_checkpoint_to_pytorch.py` | 311 | 2,946 |
| `transformers/src/transformers/models/xlm/modeling_tf_xlm.py` | 4,388 | 52,345 |
| `transformers/src/transformers/models/xlm/modeling_xlm.py` | 4,826 | 55,173 |
| `transformers/src/transformers/models/xlm/tokenization_xlm.py` | 3,140 | 34,980 |
| `transformers/src/transformers/models/xlm_prophetnet/__init__.py` | 232 | 2,704 |
| `transformers/src/transformers/models/xlm_prophetnet/configuration_xlm_prophetnet.py` | 166 | 1,506 |
| `transformers/src/transformers/models/xlm_prophetnet/modeling_xlm_prophetnet.py` | 663 | 7,169 |
| `transformers/src/transformers/models/xlm_prophetnet/tokenization_xlm_prophetnet.py` | 1,437 | 13,907 |
| `transformers/src/transformers/models/xlm_roberta/__init__.py` | 358 | 5,490 |
| `transformers/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py` | 248 | 2,814 |
| `transformers/src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py` | 567 | 5,803 |
| `transformers/src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py` | 728 | 6,481 |
| `transformers/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py` | 585 | 5,647 |
| `transformers/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py` | 1,435 | 14,284 |
| `transformers/src/transformers/models/xlm_roberta/tokenization_xlm_roberta_fast.py` | 922 | 10,263 |
| `transformers/src/transformers/models/xlm_roberta_xl/__init__.py` | 215 | 2,576 |
| `transformers/src/transformers/models/xlm_roberta_xl/configuration_xlm_roberta_xl.py` | 712 | 7,572 |
| `transformers/src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py` | 557 | 8,228 |
| `transformers/src/transformers/models/xlm_roberta_xl/modeling_xlm_roberta_xl.py` | 5,288 | 68,266 |
| `transformers/src/transformers/models/xlnet/__init__.py` | 316 | 4,459 |
| `transformers/src/transformers/models/xlnet/configuration_xlnet.py` | 1,177 | 11,120 |
| `transformers/src/transformers/models/xlnet/convert_xlnet_original_tf_checkpoint_to_pytorch.py` | 334 | 3,688 |
| `transformers/src/transformers/models/xlnet/modeling_tf_xlnet.py` | 6,713 | 75,503 |
| `transformers/src/transformers/models/xlnet/modeling_xlnet.py` | 8,362 | 93,170 |
| `transformers/src/transformers/models/xlnet/tokenization_xlnet.py` | 1,439 | 14,402 |
| `transformers/src/transformers/models/xlnet/tokenization_xlnet_fast.py` | 1,035 | 10,025 |
| `transformers/src/transformers/models/yolos/__init__.py` | 226 | 2,397 |
| `transformers/src/transformers/models/yolos/configuration_yolos.py` | 721 | 7,166 |
| `transformers/src/transformers/models/yolos/convert_yolos_to_pytorch.py` | 940 | 11,120 |
| `transformers/src/transformers/models/yolos/feature_extraction_yolos.py` | 4,094 | 41,902 |
| `transformers/src/transformers/models/yolos/modeling_yolos.py` | 5,294 | 57,250 |
| `transformers/src/transformers/models/yoso/__init__.py` | 216 | 2,282 |
| `transformers/src/transformers/models/yoso/common.h` | 32 | 273 |
| `transformers/src/transformers/models/yoso/common_cuda.h` | 24 | 258 |
| `transformers/src/transformers/models/yoso/common_cuda_device.h` | 302 | 2,063 |
| `transformers/src/transformers/models/yoso/configuration_yoso.py` | 682 | 6,879 |
| `transformers/src/transformers/models/yoso/convert_yoso_pytorch_to_pytorch.py` | 368 | 4,116 |
| `transformers/src/transformers/models/yoso/fast_lsh_cumulation.cu` | 1,312 | 19,061 |
| `transformers/src/transformers/models/yoso/fast_lsh_cumulation.h` | 124 | 1,575 |
| `transformers/src/transformers/models/yoso/fast_lsh_cumulation_cuda.cu` | 3,477 | 32,870 |
| `transformers/src/transformers/models/yoso/fast_lsh_cumulation_cuda.h` | 509 | 5,490 |
| `transformers/src/transformers/models/yoso/fast_lsh_cumulation_torch.cpp` | 251 | 3,154 |
| `transformers/src/transformers/models/yoso/modeling_yoso.py` | 4,293 | 55,384 |
| `transformers/src/transformers/onnx/__init__.py` | 165 | 1,563 |
| `transformers/src/transformers/onnx/__main__.py` | 402 | 4,277 |
| `transformers/src/transformers/onnx/config.py` | 2,550 | 28,119 |
| `transformers/src/transformers/onnx/convert.py` | 1,819 | 20,126 |
| `transformers/src/transformers/onnx/features.py` | 1,203 | 20,692 |
| `transformers/src/transformers/onnx/utils.py` | 420 | 3,625 |
| `transformers/src/transformers/optimization.py` | 2,650 | 27,775 |
| `transformers/src/transformers/optimization_tf.py` | 1,479 | 15,722 |
| `transformers/src/transformers/pipelines/__init__.py` | 2,785 | 31,200 |
| `transformers/src/transformers/pipelines/audio_classification.py` | 623 | 5,840 |
| `transformers/src/transformers/pipelines/audio_utils.py` | 840 | 7,786 |
| `transformers/src/transformers/pipelines/automatic_speech_recognition.py` | 2,033 | 20,378 |
| `transformers/src/transformers/pipelines/base.py` | 4,396 | 44,867 |
| `transformers/src/transformers/pipelines/conversational.py` | 1,225 | 13,466 |
| `transformers/src/transformers/pipelines/feature_extraction.py` | 393 | 3,581 |
| `transformers/src/transformers/pipelines/fill_mask.py` | 936 | 9,913 |
| `transformers/src/transformers/pipelines/image_classification.py` | 431 | 4,368 |
| `transformers/src/transformers/pipelines/image_segmentation.py` | 727 | 8,045 |
| `transformers/src/transformers/pipelines/object_detection.py` | 518 | 5,304 |
| `transformers/src/transformers/pipelines/pt_utils.py` | 1,072 | 11,513 |
| `transformers/src/transformers/pipelines/question_answering.py` | 2,456 | 25,990 |
| `transformers/src/transformers/pipelines/table_question_answering.py` | 1,609 | 18,831 |
| `transformers/src/transformers/pipelines/text2text_generation.py` | 1,426 | 15,120 |
| `transformers/src/transformers/pipelines/text_classification.py` | 928 | 9,362 |
| `transformers/src/transformers/pipelines/text_generation.py` | 1,125 | 12,534 |
| `transformers/src/transformers/pipelines/token_classification.py` | 1,857 | 20,884 |
| `transformers/src/transformers/pipelines/visual_question_answering.py` | 481 | 5,031 |
| `transformers/src/transformers/pipelines/zero_shot_classification.py` | 1,038 | 10,826 |
| `transformers/src/transformers/pipelines/zero_shot_image_classification.py` | 469 | 5,132 |
| `transformers/src/transformers/processing_utils.py` | 1,015 | 10,559 |
| `transformers/src/transformers/py.typed` | 0 | 1 |
| `transformers/src/transformers/pytorch_utils.py` | 1,105 | 10,370 |
| `transformers/src/transformers/sagemaker/__init__.py` | 139 | 901 |
| `transformers/src/transformers/sagemaker/trainer_sm.py` | 140 | 1,044 |
| `transformers/src/transformers/sagemaker/training_args_sm.py` | 537 | 5,347 |
| `transformers/src/transformers/testing_utils.py` | 5,342 | 50,790 |
| `transformers/src/transformers/tf_utils.py` | 355 | 2,639 |
| `transformers/src/transformers/tokenization_utils.py` | 3,910 | 39,944 |
| `transformers/src/transformers/tokenization_utils_base.py` | 16,921 | 172,753 |
| `transformers/src/transformers/tokenization_utils_fast.py` | 2,866 | 33,147 |
| `transformers/src/transformers/trainer.py` | 13,284 | 160,826 |
| `transformers/src/transformers/trainer_callback.py` | 2,303 | 23,218 |
| `transformers/src/transformers/trainer_pt_utils.py` | 5,067 | 45,063 |
| `transformers/src/transformers/trainer_seq2seq.py` | 1,101 | 11,116 |
| `transformers/src/transformers/trainer_tf.py` | 2,957 | 34,693 |
| `transformers/src/transformers/trainer_utils.py` | 2,317 | 23,722 |
| `transformers/src/transformers/training_args.py` | 8,419 | 80,161 |
| `transformers/src/transformers/training_args_seq2seq.py` | 338 | 2,901 |
| `transformers/src/transformers/training_args_tf.py` | 1,475 | 14,139 |
| `transformers/src/transformers/utils/__init__.py` | 445 | 5,388 |
| `transformers/src/transformers/utils/doc.py` | 3,589 | 39,180 |
| `transformers/src/transformers/utils/dummy_detectron2_objects.py` | 35 | 391 |
| `transformers/src/transformers/utils/dummy_flax_objects.py` | 1,751 | 26,486 |
| `transformers/src/transformers/utils/dummy_pt_objects.py` | 8,147 | 124,373 |
| `transformers/src/transformers/utils/dummy_scatter_objects.py` | 84 | 1,138 |
| `transformers/src/transformers/utils/dummy_sentencepiece_and_speech_objects.py` | 34 | 342 |
| `transformers/src/transformers/utils/dummy_sentencepiece_and_tokenizers_objects.py` | 30 | 301 |
| `transformers/src/transformers/utils/dummy_sentencepiece_objects.py` | 307 | 4,716 |
| `transformers/src/transformers/utils/dummy_speech_objects.py` | 43 | 482 |
| `transformers/src/transformers/utils/dummy_tf_objects.py` | 3,588 | 52,848 |
| `transformers/src/transformers/utils/dummy_timm_and_vision_objects.py` | 76 | 903 |
| `transformers/src/transformers/utils/dummy_timm_objects.py` | 65 | 805 |
| `transformers/src/transformers/utils/dummy_tokenizers_objects.py` | 593 | 9,216 |
| `transformers/src/transformers/utils/dummy_vision_objects.py` | 274 | 3,990 |
| `transformers/src/transformers/utils/fx.py` | 3,452 | 40,281 |
| `transformers/src/transformers/utils/generic.py` | 1,063 | 10,402 |
| `transformers/src/transformers/utils/hp_naming.py` | 498 | 4,971 |
| `transformers/src/transformers/utils/hub.py` | 5,025 | 49,446 |
| `transformers/src/transformers/utils/import_utils.py` | 2,943 | 31,182 |
| `transformers/src/transformers/utils/logging.py` | 924 | 9,516 |
| `transformers/src/transformers/utils/model_parallel_utils.py` | 299 | 2,300 |
| `transformers/src/transformers/utils/notebook.py` | 1,440 | 14,576 |
| `transformers/src/transformers/utils/sentencepiece_model_pb2.py` | 1,762 | 50,686 |
| `transformers/src/transformers/utils/versions.py` | 518 | 4,420 |
| `transformers/templates/adding_a_missing_tokenization_test/README.md` | 258 | 1,808 |
| `transformers/templates/adding_a_missing_tokenization_test/cookiecutter-template-{{cookiecutter.modelname}}/test_tokenization_{{cookiecutter.lowercase_modelname}}.py` | 311 | 3,032 |
| `transformers/templates/adding_a_missing_tokenization_test/cookiecutter.json` | 23 | 333 |
| `transformers/templates/adding_a_new_example_script/README.md` | 272 | 1,745 |
| `transformers/templates/adding_a_new_example_script/cookiecutter.json` | 23 | 328 |
| `transformers/templates/adding_a_new_example_script/{{cookiecutter.directory_name}}/run_{{cookiecutter.example_shortcut}}.py` | 3,435 | 37,661 |
| `transformers/templates/adding_a_new_model/ADD_NEW_MODEL_PROPOSAL_TEMPLATE.md` | 7,667 | 51,352 |
| `transformers/templates/adding_a_new_model/README.md` | 1,517 | 9,799 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/__init__.py` | 633 | 12,478 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/configuration.json` | 20 | 582 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/configuration_{{cookiecutter.lowercase_modelname}}.py` | 1,089 | 12,062 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/modeling_flax_{{cookiecutter.lowercase_modelname}}.py` | 9,352 | 137,653 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/modeling_tf_{{cookiecutter.lowercase_modelname}}.py` | 10,816 | 144,139 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/modeling_{{cookiecutter.lowercase_modelname}}.py` | 11,715 | 155,208 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/test_modeling_flax_{{cookiecutter.lowercase_modelname}}.py` | 1,606 | 26,929 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/test_modeling_tf_{{cookiecutter.lowercase_modelname}}.py` | 2,610 | 42,611 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/test_modeling_{{cookiecutter.lowercase_modelname}}.py` | 2,424 | 44,210 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/to_replace_{{cookiecutter.lowercase_modelname}}.py` | 1,456 | 19,719 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/tokenization_fast_{{cookiecutter.lowercase_modelname}}.py` | 561 | 7,417 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/tokenization_{{cookiecutter.lowercase_modelname}}.py` | 1,087 | 12,024 |
| `transformers/templates/adding_a_new_model/cookiecutter-template-{{cookiecutter.modelname}}/{{cookiecutter.lowercase_modelname}}.mdx` | 413 | 6,258 |
| `transformers/templates/adding_a_new_model/cookiecutter.json` | 46 | 577 |
| `transformers/templates/adding_a_new_model/open_model_proposals/ADD_BIG_BIRD.md` | 7,700 | 53,317 |
| `transformers/templates/adding_a_new_model/open_model_proposals/README.md` | 10 | 103 |
| `transformers/templates/adding_a_new_model/tests/encoder-bert-tokenizer.json` | 27 | 384 |
| `transformers/templates/adding_a_new_model/tests/flax-encoder-bert-tokenizer.json` | 24 | 378 |
| `transformers/templates/adding_a_new_model/tests/flax-seq-2-seq-bart-tokenizer.json` | 24 | 390 |
| `transformers/templates/adding_a_new_model/tests/pt-encoder-bert-tokenizer.json` | 24 | 373 |
| `transformers/templates/adding_a_new_model/tests/pt-seq-2-seq-bart-tokenizer.json` | 24 | 383 |
| `transformers/templates/adding_a_new_model/tests/standalone.json` | 25 | 394 |
| `transformers/templates/adding_a_new_model/tests/tf-encoder-bert-tokenizer.json` | 24 | 376 |
| `transformers/templates/adding_a_new_model/tests/tf-seq-2-seq-bart-tokenizer.json` | 24 | 395 |
| `transformers/tests/__init__.py` | 0 | 0 |
| `transformers/tests/benchmark/__init__.py` | 0 | 0 |
| `transformers/tests/benchmark/test_benchmark.py` | 533 | 10,646 |
| `transformers/tests/benchmark/test_benchmark_tf.py` | 463 | 9,024 |
| `transformers/tests/deepspeed/ds_config_zero2.json` | 88 | 1,230 |
| `transformers/tests/deepspeed/ds_config_zero3.json` | 101 | 1,499 |
| `transformers/tests/deepspeed/test_deepspeed.py` | 3,935 | 47,317 |
| `transformers/tests/deepspeed/test_model_zoo.py` | 1,187 | 12,779 |
| `transformers/tests/deepspeed/vit_feature_extractor.json` | 6 | 72 |
| `transformers/tests/extended/test_trainer_ext.py` | 1,198 | 14,809 |
| `transformers/tests/fixtures/add_distilbert_like_config.json` | 32 | 504 |
| `transformers/tests/fixtures/dummy-config.json` | 4 | 29 |
| `transformers/tests/fixtures/dummy_feature_extractor_config.json` | 6 | 101 |
| `transformers/tests/fixtures/empty.txt` | 0 | 0 |
| `transformers/tests/fixtures/input.txt` | 11 | 52 |
| `transformers/tests/fixtures/merges.txt` | 10 | 36 |
| `transformers/tests/fixtures/preprocessor_config.json` | 6 | 100 |
| `transformers/tests/fixtures/sample_text.txt` | 742 | 4,394 |
| `transformers/tests/fixtures/sample_text_no_unicode.txt` | 730 | 4,284 |
| `transformers/tests/fixtures/spiece.model` | — | 760,289 |
| `transformers/tests/fixtures/test_entity_vocab.json` | 12 | 76 |
| `transformers/tests/fixtures/test_sentencepiece.model` | — | 253,154 |
| `transformers/tests/fixtures/test_sentencepiece_bpe.model` | — | 251,527 |
| `transformers/tests/fixtures/test_sentencepiece_no_bos.model` | — | 253,134 |
| `transformers/tests/fixtures/test_sentencepiece_with_bytefallback.model` | — | 270,096 |
| `transformers/tests/fixtures/tests_samples/.gitignore` | 6 | 52 |
| `transformers/tests/fixtures/tests_samples/COCO/000000039769.png` | — | 694,498 |
| `transformers/tests/fixtures/tests_samples/COCO/coco_annotations.txt` | 512 | 4,075 |
| `transformers/tests/fixtures/tests_samples/COCO/coco_panoptic/000000039769.png` | — | 8,269 |
| `transformers/tests/fixtures/tests_samples/COCO/coco_panoptic_annotations.txt` | 78 | 555 |
| `transformers/tests/fixtures/tests_samples/GermEval/dev.txt` | 384 | 1,718 |
| `transformers/tests/fixtures/tests_samples/GermEval/labels.txt` | 25 | 218 |
| `transformers/tests/fixtures/tests_samples/GermEval/train.txt` | 380 | 1,779 |
| `transformers/tests/fixtures/tests_samples/MRPC/dev.csv` | 232 | 1,354 |
| `transformers/tests/fixtures/tests_samples/MRPC/dev.tsv` | 264 | 1,386 |
| `transformers/tests/fixtures/tests_samples/MRPC/train.csv` | 232 | 1,354 |
| `transformers/tests/fixtures/tests_samples/MRPC/train.tsv` | 264 | 1,386 |
| `transformers/tests/fixtures/tests_samples/SQUAD/sample.json` | 2,144 | 17,233 |
| `transformers/tests/fixtures/tests_samples/STS-B/dev.tsv` | 201 | 1,126 |
| `transformers/tests/fixtures/tests_samples/STS-B/train.tsv` | 194 | 1,121 |
| `transformers/tests/fixtures/tests_samples/conll/sample.json` | 410 | 3,001 |
| `transformers/tests/fixtures/tests_samples/swag/sample.json` | 528 | 3,522 |
| `transformers/tests/fixtures/tests_samples/wiki_text/wiki_00` | 11,757 | 79,924 |
| `transformers/tests/fixtures/tests_samples/wmt16/sample.json` | 166 | 1,423 |
| `transformers/tests/fixtures/tests_samples/wmt_en_ro/test.json` | 4,373 | 27,417 |
| `transformers/tests/fixtures/tests_samples/wmt_en_ro/train.json` | 1,510 | 11,234 |
| `transformers/tests/fixtures/tests_samples/wmt_en_ro/val.json` | 3,586 | 21,699 |
| `transformers/tests/fixtures/tests_samples/xsum/sample.json` | 2,531 | 15,601 |
| `transformers/tests/fixtures/vocab.json` | 42 | 228 |
| `transformers/tests/fixtures/vocab.txt` | 10 | 85 |
| `transformers/tests/generation/__init__.py` | 0 | 0 |
| `transformers/tests/generation/test_generation_beam_constraints.py` | 470 | 4,445 |
| `transformers/tests/generation/test_generation_beam_search.py` | 1,769 | 25,087 |
| `transformers/tests/generation/test_generation_flax_logits_process.py` | 1,091 | 12,721 |
| `transformers/tests/generation/test_generation_flax_utils.py` | 753 | 10,650 |
| `transformers/tests/generation/test_generation_logits_process.py` | 2,003 | 23,483 |
| `transformers/tests/generation/test_generation_stopping_criteria.py` | 271 | 3,613 |
| `transformers/tests/generation/test_generation_tf_logits_process.py` | 1,488 | 17,555 |
| `transformers/tests/generation/test_generation_utils.py` | 6,392 | 115,750 |
| `transformers/tests/models/__init__.py` | 0 | 0 |
| `transformers/tests/models/albert/__init__.py` | 0 | 0 |
| `transformers/tests/models/albert/test_modeling_albert.py` | 763 | 12,904 |
| `transformers/tests/models/albert/test_modeling_flax_albert.py` | 400 | 5,974 |
| `transformers/tests/models/albert/test_modeling_tf_albert.py` | 844 | 13,754 |
| `transformers/tests/models/albert/test_tokenization_albert.py` | 1,318 | 8,118 |
| `transformers/tests/models/auto/__init__.py` | 0 | 0 |
| `transformers/tests/models/auto/test_configuration_auto.py` | 366 | 4,748 |
| `transformers/tests/models/auto/test_feature_extraction_auto.py` | 379 | 5,474 |
| `transformers/tests/models/auto/test_modeling_auto.py` | 855 | 15,626 |
| `transformers/tests/models/auto/test_modeling_flax_auto.py` | 314 | 4,171 |
| `transformers/tests/models/auto/test_modeling_tf_auto.py` | 663 | 12,195 |
| `transformers/tests/models/auto/test_modeling_tf_pytorch.py` | 508 | 10,044 |
| `transformers/tests/models/auto/test_processor_auto.py` | 792 | 13,595 |
| `transformers/tests/models/auto/test_tokenization_auto.py` | 955 | 15,820 |
| `transformers/tests/models/bart/__init__.py` | 0 | 0 |
| `transformers/tests/models/bart/test_modeling_bart.py` | 9,941 | 89,729 |
| `transformers/tests/models/bart/test_modeling_flax_bart.py` | 4,697 | 44,969 |
| `transformers/tests/models/bart/test_modeling_tf_bart.py` | 9,575 | 77,589 |
| `transformers/tests/models/bart/test_tokenization_bart.py` | 599 | 8,274 |
| `transformers/tests/models/barthez/__init__.py` | 0 | 0 |
| `transformers/tests/models/barthez/test_tokenization_barthez.py` | 614 | 5,574 |
| `transformers/tests/models/bartpho/__init__.py` | 0 | 0 |
| `transformers/tests/models/bartpho/test_tokenization_bartpho.py` | 240 | 2,638 |
| `transformers/tests/models/beit/__init__.py` | 0 | 0 |
| `transformers/tests/models/beit/test_feature_extraction_beit.py` | 710 | 12,575 |
| `transformers/tests/models/beit/test_modeling_beit.py` | 1,157 | 17,571 |
| `transformers/tests/models/beit/test_modeling_flax_beit.py` | 760 | 11,412 |
| `transformers/tests/models/bert/__init__.py` | 0 | 0 |
| `transformers/tests/models/bert/test_modeling_bert.py` | 1,374 | 25,159 |
| `transformers/tests/models/bert/test_modeling_flax_bert.py` | 386 | 5,928 |
| `transformers/tests/models/bert/test_modeling_tf_bert.py` | 1,813 | 30,061 |
| `transformers/tests/models/bert/test_tokenization_bert.py` | 894 | 13,961 |
| `transformers/tests/models/bert_generation/__init__.py` | 0 | 0 |
| `transformers/tests/models/bert_generation/test_modeling_bert_generation.py` | 727 | 12,426 |
| `transformers/tests/models/bert_generation/test_tokenization_bert_generation.py` | 1,106 | 9,495 |
| `transformers/tests/models/bert_japanese/__init__.py` | 0 | 0 |
| `transformers/tests/models/bert_japanese/test_tokenization_bert_japanese.py` | 942 | 12,468 |
| `transformers/tests/models/bertweet/__init__.py` | 0 | 0 |
| `transformers/tests/models/bertweet/test_tokenization_bertweet.py` | 277 | 2,719 |
| `transformers/tests/models/big_bird/__init__.py` | 0 | 0 |
| `transformers/tests/models/big_bird/test_modeling_big_bird.py` | 3,075 | 42,929 |
| `transformers/tests/models/big_bird/test_modeling_flax_big_bird.py` | 554 | 8,625 |
| `transformers/tests/models/big_bird/test_tokenization_big_bird.py` | 1,255 | 10,705 |
| `transformers/tests/models/bigbird_pegasus/__init__.py` | 0 | 0 |
| `transformers/tests/models/bigbird_pegasus/test_modeling_bigbird_pegasus.py` | 16,240 | 110,130 |
| `transformers/tests/models/blenderbot/__init__.py` | 0 | 0 |
| `transformers/tests/models/blenderbot/test_modeling_blenderbot.py` | 1,378 | 21,738 |
| `transformers/tests/models/blenderbot/test_modeling_flax_blenderbot.py` | 1,113 | 17,288 |
| `transformers/tests/models/blenderbot/test_modeling_tf_blenderbot.py` | 932 | 13,502 |
| `transformers/tests/models/blenderbot/test_tokenization_blenderbot.py` | 215 | 2,284 |
| `transformers/tests/models/blenderbot_small/__init__.py` | 0 | 0 |
| `transformers/tests/models/blenderbot_small/test_modeling_blenderbot_small.py` | 1,386 | 21,586 |
| `transformers/tests/models/blenderbot_small/test_modeling_flax_blenderbot_small.py` | 1,048 | 16,390 |
| `transformers/tests/models/blenderbot_small/test_modeling_tf_blenderbot_small.py` | 1,000 | 14,068 |
| `transformers/tests/models/blenderbot_small/test_tokenization_blenderbot_small.py` | 335 | 3,632 |
| `transformers/tests/models/bloom/__init__.py` | 0 | 0 |
| `transformers/tests/models/bloom/test_modeling_bloom.py` | 2,050 | 32,526 |
| `transformers/tests/models/bloom/test_tokenization_bloom.py` | 484 | 5,960 |
| `transformers/tests/models/bort/__init__.py` | 0 | 0 |
| `transformers/tests/models/bort/test_modeling_bort.py` | 202 | 1,894 |
| `transformers/tests/models/bort/test_modeling_tf_bort.py` | 204 | 1,843 |
| `transformers/tests/models/byt5/__init__.py` | 0 | 0 |
| `transformers/tests/models/byt5/test_tokenization_byt5.py` | 1,358 | 17,451 |
| `transformers/tests/models/camembert/__init__.py` | 0 | 0 |
| `transformers/tests/models/camembert/test_modeling_camembert.py` | 207 | 2,039 |
| `transformers/tests/models/camembert/test_modeling_tf_camembert.py` | 209 | 1,996 |
| `transformers/tests/models/camembert/test_tokenization_camembert.py` | 620 | 5,811 |
| `transformers/tests/models/canine/__init__.py` | 0 | 0 |
| `transformers/tests/models/canine/test_modeling_canine.py` | 5,562 | 37,451 |
| `transformers/tests/models/canine/test_tokenization_canine.py` | 1,117 | 16,163 |
| `transformers/tests/models/clip/__init__.py` | 0 | 0 |
| `transformers/tests/models/clip/test_feature_extraction_clip.py` | 663 | 11,071 |
| `transformers/tests/models/clip/test_modeling_clip.py` | 1,792 | 26,052 |
| `transformers/tests/models/clip/test_modeling_flax_clip.py` | 1,498 | 24,253 |
| `transformers/tests/models/clip/test_modeling_tf_clip.py` | 1,741 | 26,431 |
| `transformers/tests/models/clip/test_processor_clip.py` | 542 | 8,038 |
| `transformers/tests/models/clip/test_tokenization_clip.py` | 705 | 8,538 |
| `transformers/tests/models/codegen/__init__.py` | 0 | 0 |
| `transformers/tests/models/codegen/test_modeling_codegen.py` | 1,405 | 23,649 |
| `transformers/tests/models/codegen/test_tokenization_codegen.py` | 869 | 10,633 |
| `transformers/tests/models/convbert/__init__.py` | 0 | 0 |
| `transformers/tests/models/convbert/test_modeling_convbert.py` | 1,098 | 19,389 |
| `transformers/tests/models/convbert/test_modeling_tf_convbert.py` | 982 | 16,733 |
| `transformers/tests/models/convnext/__init__.py` | 0 | 0 |
| `transformers/tests/models/convnext/test_feature_extraction_convnext.py` | 422 | 6,840 |
| `transformers/tests/models/convnext/test_modeling_convnext.py` | 658 | 9,631 |
| `transformers/tests/models/convnext/test_modeling_tf_convnext.py` | 815 | 11,631 |
| `transformers/tests/models/cpm/__init__.py` | 0 | 0 |
| `transformers/tests/models/cpm/test_tokenization_cpm.py` | 183 | 1,703 |
| `transformers/tests/models/ctrl/__init__.py` | 0 | 0 |
| `transformers/tests/models/ctrl/test_modeling_ctrl.py` | 606 | 8,708 |
| `transformers/tests/models/ctrl/test_modeling_tf_ctrl.py` | 671 | 9,589 |
| `transformers/tests/models/ctrl/test_tokenization_ctrl.py` | 265 | 2,662 |
| `transformers/tests/models/cvt/__init__.py` | 0 | 0 |
| `transformers/tests/models/cvt/test_modeling_cvt.py` | 717 | 10,506 |
| `transformers/tests/models/data2vec/__init__.py` | 0 | 0 |
| `transformers/tests/models/data2vec/test_modeling_data2vec_audio.py` | 2,008 | 29,540 |
| `transformers/tests/models/data2vec/test_modeling_data2vec_text.py` | 1,223 | 20,514 |
| `transformers/tests/models/data2vec/test_modeling_data2vec_vision.py` | 943 | 13,721 |
| `transformers/tests/models/data2vec/test_modeling_tf_data2vec_vision.py` | 1,473 | 22,013 |
| `transformers/tests/models/deberta/__init__.py` | 0 | 0 |
| `transformers/tests/models/deberta/test_modeling_deberta.py` | 687 | 11,554 |
| `transformers/tests/models/deberta/test_modeling_tf_deberta.py` | 653 | 10,341 |
| `transformers/tests/models/deberta/test_tokenization_deberta.py` | 926 | 7,761 |
| `transformers/tests/models/deberta_v2/__init__.py` | 0 | 0 |
| `transformers/tests/models/deberta_v2/test_modeling_deberta_v2.py` | 725 | 12,659 |
| `transformers/tests/models/deberta_v2/test_modeling_tf_deberta_v2.py` | 651 | 10,574 |
| `transformers/tests/models/deberta_v2/test_tokenization_deberta_v2.py` | 1,577 | 13,907 |
| `transformers/tests/models/decision_transformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/decision_transformer/test_modeling_decision_transformer.py` | 695 | 9,458 |
| `transformers/tests/models/deit/__init__.py` | 0 | 0 |
| `transformers/tests/models/deit/test_feature_extraction_deit.py` | 430 | 7,079 |
| `transformers/tests/models/deit/test_modeling_deit.py` | 1,002 | 15,249 |
| `transformers/tests/models/detr/__init__.py` | 0 | 0 |
| `transformers/tests/models/detr/test_feature_extraction_detr.py` | 948 | 14,414 |
| `transformers/tests/models/detr/test_modeling_detr.py` | 1,388 | 22,582 |
| `transformers/tests/models/distilbert/__init__.py` | 0 | 0 |
| `transformers/tests/models/distilbert/test_modeling_distilbert.py` | 709 | 12,090 |
| `transformers/tests/models/distilbert/test_modeling_flax_distilbert.py` | 381 | 5,644 |
| `transformers/tests/models/distilbert/test_modeling_tf_distilbert.py` | 622 | 9,832 |
| `transformers/tests/models/distilbert/test_tokenization_distilbert.py` | 172 | 1,720 |
| `transformers/tests/models/dit/__init__.py` | 0 | 0 |
| `transformers/tests/models/dit/test_modeling_dit.py` | 187 | 2,055 |
| `transformers/tests/models/dpr/__init__.py` | 0 | 0 |
| `transformers/tests/models/dpr/test_modeling_dpr.py` | 711 | 11,721 |
| `transformers/tests/models/dpr/test_modeling_tf_dpr.py` | 595 | 9,762 |
| `transformers/tests/models/dpr/test_tokenization_dpr.py` | 285 | 3,515 |
| `transformers/tests/models/dpt/__init__.py` | 0 | 0 |
| `transformers/tests/models/dpt/test_feature_extraction_dpt.py` | 411 | 6,611 |
| `transformers/tests/models/dpt/test_modeling_dpt.py` | 774 | 11,474 |
| `transformers/tests/models/electra/__init__.py` | 0 | 0 |
| `transformers/tests/models/electra/test_modeling_electra.py` | 892 | 16,536 |
| `transformers/tests/models/electra/test_modeling_flax_electra.py` | 249 | 4,941 |
| `transformers/tests/models/electra/test_modeling_tf_electra.py` | 1,496 | 24,021 |
| `transformers/tests/models/encoder_decoder/__init__.py` | 0 | 0 |
| `transformers/tests/models/encoder_decoder/test_modeling_encoder_decoder.py` | 3,493 | 49,941 |
| `transformers/tests/models/encoder_decoder/test_modeling_flax_encoder_decoder.py` | 1,788 | 27,689 |
| `transformers/tests/models/encoder_decoder/test_modeling_tf_encoder_decoder.py` | 3,350 | 50,906 |
| `transformers/tests/models/flaubert/__init__.py` | 0 | 0 |
| `transformers/tests/models/flaubert/test_modeling_flaubert.py` | 898 | 16,079 |
| `transformers/tests/models/flaubert/test_modeling_tf_flaubert.py` | 772 | 12,504 |
| `transformers/tests/models/flava/__init__.py` | 0 | 0 |
| `transformers/tests/models/flava/test_feature_extraction_flava.py` | 753 | 14,024 |
| `transformers/tests/models/flava/test_modeling_flava.py` | 2,859 | 47,220 |
| `transformers/tests/models/flava/test_processor_flava.py` | 602 | 9,473 |
| `transformers/tests/models/fnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/fnet/test_modeling_fnet.py` | 1,373 | 23,386 |
| `transformers/tests/models/fnet/test_tokenization_fnet.py` | 2,158 | 23,096 |
| `transformers/tests/models/fsmt/__init__.py` | 0 | 0 |
| `transformers/tests/models/fsmt/test_modeling_fsmt.py` | 1,537 | 21,362 |
| `transformers/tests/models/fsmt/test_tokenization_fsmt.py` | 552 | 6,441 |
| `transformers/tests/models/funnel/__init__.py` | 0 | 0 |
| `transformers/tests/models/funnel/test_modeling_funnel.py` | 1,224 | 19,449 |
| `transformers/tests/models/funnel/test_modeling_tf_funnel.py` | 976 | 14,869 |
| `transformers/tests/models/funnel/test_tokenization_funnel.py` | 256 | 2,984 |
| `transformers/tests/models/glpn/__init__.py` | 0 | 0 |
| `transformers/tests/models/glpn/test_feature_extraction_glpn.py` | 363 | 5,021 |
| `transformers/tests/models/glpn/test_modeling_glpn.py` | 934 | 14,246 |
| `transformers/tests/models/gpt2/__init__.py` | 0 | 0 |
| `transformers/tests/models/gpt2/test_modeling_flax_gpt2.py` | 984 | 14,852 |
| `transformers/tests/models/gpt2/test_modeling_gpt2.py` | 1,947 | 32,916 |
| `transformers/tests/models/gpt2/test_modeling_tf_gpt2.py` | 1,934 | 26,885 |
| `transformers/tests/models/gpt2/test_tokenization_gpt2.py` | 820 | 9,979 |
| `transformers/tests/models/gpt_neo/__init__.py` | 0 | 0 |
| `transformers/tests/models/gpt_neo/test_modeling_flax_gpt_neo.py` | 969 | 14,734 |
| `transformers/tests/models/gpt_neo/test_modeling_gpt_neo.py` | 1,543 | 23,108 |
| `transformers/tests/models/gpt_neox/__init__.py` | 0 | 0 |
| `transformers/tests/models/gpt_neox/test_modeling_gpt_neox.py` | 665 | 10,255 |
| `transformers/tests/models/gptj/__init__.py` | 0 | 0 |
| `transformers/tests/models/gptj/test_modeling_flax_gptj.py` | 962 | 14,528 |
| `transformers/tests/models/gptj/test_modeling_gptj.py` | 1,558 | 24,370 |
| `transformers/tests/models/gptj/test_modeling_tf_gptj.py` | 1,501 | 21,674 |
| `transformers/tests/models/herbert/__init__.py` | 0 | 0 |
| `transformers/tests/models/herbert/test_tokenization_herbert.py` | 362 | 4,455 |
| `transformers/tests/models/hubert/__init__.py` | 0 | 0 |
| `transformers/tests/models/hubert/test_modeling_hubert.py` | 2,556 | 38,677 |
| `transformers/tests/models/hubert/test_modeling_tf_hubert.py` | 1,507 | 22,236 |
| `transformers/tests/models/ibert/__init__.py` | 0 | 0 |
| `transformers/tests/models/ibert/test_modeling_ibert.py` | 2,224 | 30,386 |
| `transformers/tests/models/imagegpt/__init__.py` | 0 | 0 |
| `transformers/tests/models/imagegpt/test_feature_extraction_imagegpt.py` | 417 | 6,198 |
| `transformers/tests/models/imagegpt/test_modeling_imagegpt.py` | 1,470 | 22,025 |
| `transformers/tests/models/layoutlm/__init__.py` | 0 | 0 |
| `transformers/tests/models/layoutlm/test_modeling_layoutlm.py` | 980 | 14,947 |
| `transformers/tests/models/layoutlm/test_modeling_tf_layoutlm.py` | 938 | 14,203 |
| `transformers/tests/models/layoutlm/test_tokenization_layoutlm.py` | 243 | 2,604 |
| `transformers/tests/models/layoutlmv2/__init__.py` | 0 | 0 |
| `transformers/tests/models/layoutlmv2/test_feature_extraction_layoutlmv2.py` | 1,339 | 12,929 |
| `transformers/tests/models/layoutlmv2/test_modeling_layoutlmv2.py` | 1,377 | 22,605 |
| `transformers/tests/models/layoutlmv2/test_processor_layoutlmv2.py` | 2,241 | 24,061 |
| `transformers/tests/models/layoutlmv2/test_tokenization_layoutlmv2.py` | 8,792 | 126,949 |
| `transformers/tests/models/layoutlmv3/__init__.py` | 0 | 0 |
| `transformers/tests/models/layoutlmv3/test_feature_extraction_layoutlmv3.py` | 1,335 | 12,815 |
| `transformers/tests/models/layoutlmv3/test_modeling_layoutlmv3.py` | 969 | 15,643 |
| `transformers/tests/models/layoutlmv3/test_processor_layoutlmv3.py` | 1,974 | 23,016 |
| `transformers/tests/models/layoutlmv3/test_tokenization_layoutlmv3.py` | 8,470 | 122,796 |
| `transformers/tests/models/layoutxlm/__init__.py` | 0 | 0 |
| `transformers/tests/models/layoutxlm/test_processor_layoutxlm.py` | 1,902 | 22,041 |
| `transformers/tests/models/layoutxlm/test_tokenization_layoutxlm.py` | 7,090 | 97,455 |
| `transformers/tests/models/led/__init__.py` | 0 | 0 |
| `transformers/tests/models/led/test_modeling_led.py` | 14,577 | 95,343 |
| `transformers/tests/models/led/test_modeling_tf_led.py` | 1,292 | 18,745 |
| `transformers/tests/models/levit/__init__.py` | 0 | 0 |
| `transformers/tests/models/levit/test_feature_extraction_levit.py` | 422 | 6,859 |
| `transformers/tests/models/levit/test_modeling_levit.py` | 1,111 | 16,497 |
| `transformers/tests/models/longformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/longformer/test_modeling_longformer.py` | 1,780 | 29,951 |
| `transformers/tests/models/longformer/test_modeling_tf_longformer.py` | 1,900 | 30,382 |
| `transformers/tests/models/longt5/__init__.py` | 0 | 0 |
| `transformers/tests/models/longt5/test_modeling_flax_longt5.py` | 4,109 | 44,188 |
| `transformers/tests/models/longt5/test_modeling_longt5.py` | 5,334 | 67,280 |
| `transformers/tests/models/luke/__init__.py` | 0 | 0 |
| `transformers/tests/models/luke/test_modeling_luke.py` | 1,450 | 27,293 |
| `transformers/tests/models/luke/test_tokenization_luke.py` | 2,420 | 30,186 |
| `transformers/tests/models/lxmert/__init__.py` | 0 | 0 |
| `transformers/tests/models/lxmert/test_modeling_lxmert.py` | 1,580 | 30,668 |
| `transformers/tests/models/lxmert/test_modeling_tf_lxmert.py` | 1,506 | 28,716 |
| `transformers/tests/models/lxmert/test_tokenization_lxmert.py` | 262 | 3,038 |
| `transformers/tests/models/m2m_100/__init__.py` | 0 | 0 |
| `transformers/tests/models/m2m_100/test_modeling_m2m_100.py` | 1,174 | 16,724 |
| `transformers/tests/models/m2m_100/test_tokenization_m2m_100.py` | 1,326 | 12,018 |
| `transformers/tests/models/marian/__init__.py` | 0 | 0 |
| `transformers/tests/models/marian/test_modeling_flax_marian.py` | 1,272 | 18,411 |
| `transformers/tests/models/marian/test_modeling_marian.py` | 2,217 | 32,630 |
| `transformers/tests/models/marian/test_modeling_tf_marian.py` | 1,271 | 17,770 |
| `transformers/tests/models/marian/test_tokenization_marian.py` | 1,053 | 8,596 |
| `transformers/tests/models/maskformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/maskformer/test_feature_extraction_maskformer.py` | 986 | 16,572 |
| `transformers/tests/models/maskformer/test_modeling_maskformer.py` | 1,138 | 17,499 |
| `transformers/tests/models/mbart/__init__.py` | 0 | 0 |
| `transformers/tests/models/mbart/test_modeling_flax_mbart.py` | 1,190 | 18,951 |
| `transformers/tests/models/mbart/test_modeling_mbart.py` | 1,758 | 26,519 |
| `transformers/tests/models/mbart/test_modeling_tf_mbart.py` | 988 | 14,320 |
| `transformers/tests/models/mbart/test_tokenization_mbart.py` | 1,049 | 14,012 |
| `transformers/tests/models/mbart50/__init__.py` | 0 | 0 |
| `transformers/tests/models/mbart50/test_tokenization_mbart50.py` | 1,744 | 16,981 |
| `transformers/tests/models/mctct/__init__.py` | 0 | 0 |
| `transformers/tests/models/mctct/test_feature_extraction_mctct.py` | 780 | 11,994 |
| `transformers/tests/models/mctct/test_modeling_mctct.py` | 1,749 | 26,287 |
| `transformers/tests/models/mctct/test_processor_mctct.py` | 416 | 5,982 |
| `transformers/tests/models/megatron_bert/__init__.py` | 0 | 0 |
| `transformers/tests/models/megatron_bert/test_modeling_megatron_bert.py` | 892 | 15,883 |
| `transformers/tests/models/megatron_gpt2/__init__.py` | 0 | 0 |
| `transformers/tests/models/megatron_gpt2/test_modeling_megatron_gpt2.py` | 243 | 2,656 |
| `transformers/tests/models/mluke/__init__.py` | 0 | 0 |
| `transformers/tests/models/mluke/test_tokenization_mluke.py` | 2,478 | 30,729 |
| `transformers/tests/models/mobilebert/__init__.py` | 0 | 0 |
| `transformers/tests/models/mobilebert/test_modeling_mobilebert.py` | 889 | 15,385 |
| `transformers/tests/models/mobilebert/test_modeling_tf_mobilebert.py` | 852 | 15,166 |
| `transformers/tests/models/mobilebert/test_tokenization_mobilebert.py` | 930 | 14,417 |
| `transformers/tests/models/mpnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/mpnet/test_modeling_mpnet.py` | 600 | 10,012 |
| `transformers/tests/models/mpnet/test_modeling_tf_mpnet.py` | 642 | 10,455 |
| `transformers/tests/models/mpnet/test_tokenization_mpnet.py` | 258 | 2,868 |
| `transformers/tests/models/mt5/__init__.py` | 0 | 0 |
| `transformers/tests/models/mt5/test_modeling_flax_mt5.py` | 227 | 2,539 |
| `transformers/tests/models/mt5/test_modeling_mt5.py` | 207 | 2,195 |
| `transformers/tests/models/mt5/test_modeling_tf_mt5.py` | 284 | 3,171 |
| `transformers/tests/models/nezha/__init__.py` | 0 | 0 |
| `transformers/tests/models/nezha/test_modeling_nezha.py` | 1,052 | 19,158 |
| `transformers/tests/models/nystromformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/nystromformer/test_modeling_nystromformer.py` | 725 | 12,750 |
| `transformers/tests/models/openai/__init__.py` | 0 | 0 |
| `transformers/tests/models/openai/test_modeling_openai.py` | 635 | 10,044 |
| `transformers/tests/models/openai/test_modeling_tf_openai.py` | 714 | 10,722 |
| `transformers/tests/models/openai/test_tokenization_openai.py` | 412 | 5,019 |
| `transformers/tests/models/opt/__init__.py` | 0 | 0 |
| `transformers/tests/models/opt/test_modeling_flax_opt.py` | 1,210 | 16,000 |
| `transformers/tests/models/opt/test_modeling_opt.py` | 1,198 | 16,501 |
| `transformers/tests/models/opt/test_modeling_tf_opt.py` | 1,227 | 16,851 |
| `transformers/tests/models/pegasus/__init__.py` | 0 | 0 |
| `transformers/tests/models/pegasus/test_modeling_flax_pegasus.py` | 1,197 | 15,723 |
| `transformers/tests/models/pegasus/test_modeling_pegasus.py` | 1,751 | 24,212 |
| `transformers/tests/models/pegasus/test_modeling_tf_pegasus.py` | 1,458 | 17,759 |
| `transformers/tests/models/pegasus/test_tokenization_pegasus.py` | 1,253 | 10,942 |
| `transformers/tests/models/perceiver/__init__.py` | 0 | 0 |
| `transformers/tests/models/perceiver/test_modeling_perceiver.py` | 2,726 | 44,172 |
| `transformers/tests/models/perceiver/test_tokenization_perceiver.py` | 1,102 | 13,794 |
| `transformers/tests/models/phobert/__init__.py` | 0 | 0 |
| `transformers/tests/models/phobert/test_tokenization_phobert.py` | 284 | 2,776 |
| `transformers/tests/models/plbart/__init__.py` | 0 | 0 |
| `transformers/tests/models/plbart/test_modeling_plbart.py` | 1,663 | 25,696 |
| `transformers/tests/models/plbart/test_tokenization_plbart.py` | 882 | 12,796 |
| `transformers/tests/models/poolformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/poolformer/test_feature_extraction_poolformer.py` | 418 | 6,883 |
| `transformers/tests/models/poolformer/test_modeling_poolformer.py` | 629 | 9,200 |
| `transformers/tests/models/prophetnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/prophetnet/test_modeling_prophetnet.py` | 3,059 | 52,678 |
| `transformers/tests/models/prophetnet/test_tokenization_prophetnet.py` | 549 | 7,824 |
| `transformers/tests/models/qdqbert/__init__.py` | 0 | 0 |
| `transformers/tests/models/qdqbert/test_modeling_qdqbert.py` | 1,256 | 22,354 |
| `transformers/tests/models/rag/__init__.py` | 0 | 0 |
| `transformers/tests/models/rag/test_modeling_rag.py` | 2,498 | 45,371 |
| `transformers/tests/models/rag/test_modeling_tf_rag.py` | 2,136 | 40,546 |
| `transformers/tests/models/rag/test_retrieval_rag.py` | 1,034 | 17,510 |
| `transformers/tests/models/rag/test_tokenization_rag.py` | 630 | 7,359 |
| `transformers/tests/models/realm/__init__.py` | 0 | 0 |
| `transformers/tests/models/realm/test_modeling_realm.py` | 1,212 | 20,563 |
| `transformers/tests/models/realm/test_retrieval_realm.py` | 505 | 6,945 |
| `transformers/tests/models/realm/test_tokenization_realm.py` | 839 | 13,015 |
| `transformers/tests/models/reformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/reformer/test_modeling_reformer.py` | 3,034 | 52,178 |
| `transformers/tests/models/reformer/test_tokenization_reformer.py` | 960 | 11,958 |
| `transformers/tests/models/regnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/regnet/test_modeling_regnet.py` | 713 | 10,292 |
| `transformers/tests/models/rembert/__init__.py` | 0 | 0 |
| `transformers/tests/models/rembert/test_modeling_rembert.py` | 1,072 | 19,477 |
| `transformers/tests/models/rembert/test_modeling_tf_rembert.py` | 1,681 | 27,455 |
| `transformers/tests/models/resnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/resnet/test_modeling_resnet.py` | 713 | 10,288 |
| `transformers/tests/models/retribert/__init__.py` | 0 | 0 |
| `transformers/tests/models/retribert/test_tokenization_retribert.py` | 1,041 | 16,133 |
| `transformers/tests/models/roberta/__init__.py` | 0 | 0 |
| `transformers/tests/models/roberta/test_modeling_flax_roberta.py` | 368 | 5,810 |
| `transformers/tests/models/roberta/test_modeling_roberta.py` | 1,394 | 22,587 |
| `transformers/tests/models/roberta/test_modeling_tf_roberta.py` | 1,785 | 27,412 |
| `transformers/tests/models/roberta/test_tokenization_roberta.py` | 947 | 14,569 |
| `transformers/tests/models/roformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/roformer/test_modeling_flax_roformer.py` | 385 | 5,861 |
| `transformers/tests/models/roformer/test_modeling_roformer.py` | 1,263 | 21,931 |
| `transformers/tests/models/roformer/test_modeling_tf_roformer.py` | 1,017 | 15,545 |
| `transformers/tests/models/roformer/test_tokenization_roformer.py` | 268 | 3,029 |
| `transformers/tests/models/segformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/segformer/test_feature_extraction_segformer.py` | 692 | 12,134 |
| `transformers/tests/models/segformer/test_modeling_segformer.py` | 1,022 | 15,699 |
| `transformers/tests/models/sew/__init__.py` | 0 | 0 |
| `transformers/tests/models/sew/test_modeling_sew.py` | 1,506 | 21,719 |
| `transformers/tests/models/sew_d/__init__.py` | 0 | 0 |
| `transformers/tests/models/sew_d/test_modeling_sew_d.py` | 1,533 | 22,344 |
| `transformers/tests/models/speech_encoder_decoder/__init__.py` | 0 | 0 |
| `transformers/tests/models/speech_encoder_decoder/test_modeling_flax_speech_encoder_decoder.py` | 2,304 | 39,511 |
| `transformers/tests/models/speech_encoder_decoder/test_modeling_speech_encoder_decoder.py` | 1,224 | 24,272 |
| `transformers/tests/models/speech_to_text/__init__.py` | 0 | 0 |
| `transformers/tests/models/speech_to_text/test_feature_extraction_speech_to_text.py` | 729 | 10,985 |
| `transformers/tests/models/speech_to_text/test_modeling_speech_to_text.py` | 2,378 | 38,082 |
| `transformers/tests/models/speech_to_text/test_modeling_tf_speech_to_text.py` | 1,690 | 26,300 |
| `transformers/tests/models/speech_to_text/test_processor_speech_to_text.py` | 386 | 5,982 |
| `transformers/tests/models/speech_to_text/test_tokenization_speech_to_text.py` | 1,576 | 10,298 |
| `transformers/tests/models/speech_to_text_2/__init__.py` | 0 | 0 |
| `transformers/tests/models/speech_to_text_2/test_modeling_speech_to_text_2.py` | 522 | 7,366 |
| `transformers/tests/models/speech_to_text_2/test_tokenization_speech_to_text_2.py` | 322 | 3,849 |
| `transformers/tests/models/splinter/__init__.py` | 0 | 0 |
| `transformers/tests/models/splinter/test_modeling_splinter.py` | 1,398 | 20,353 |
| `transformers/tests/models/squeezebert/__init__.py` | 0 | 0 |
| `transformers/tests/models/squeezebert/test_modeling_squeezebert.py` | 656 | 11,658 |
| `transformers/tests/models/squeezebert/test_tokenization_squeezebert.py` | 180 | 1,880 |
| `transformers/tests/models/swin/__init__.py` | 0 | 0 |
| `transformers/tests/models/swin/test_modeling_swin.py` | 1,391 | 22,258 |
| `transformers/tests/models/swin/test_modeling_tf_swin.py` | 974 | 15,818 |
| `transformers/tests/models/t5/__init__.py` | 0 | 0 |
| `transformers/tests/models/t5/test_modeling_flax_t5.py` | 4,860 | 46,958 |
| `transformers/tests/models/t5/test_modeling_t5.py` | 5,807 | 63,992 |
| `transformers/tests/models/t5/test_modeling_tf_t5.py` | 5,667 | 56,347 |
| `transformers/tests/models/t5/test_tokenization_t5.py` | 1,777 | 18,423 |
| `transformers/tests/models/tapas/__init__.py` | 0 | 0 |
| `transformers/tests/models/tapas/test_modeling_tapas.py` | 2,899 | 44,620 |
| `transformers/tests/models/tapas/test_modeling_tf_tapas.py` | 2,795 | 42,568 |
| `transformers/tests/models/tapas/test_tokenization_tapas.py` | 3,879 | 63,508 |
| `transformers/tests/models/tapex/__init__.py` | 0 | 0 |
| `transformers/tests/models/tapex/test_tokenization_tapex.py` | 2,982 | 45,264 |
| `transformers/tests/models/trajectory_transformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/trajectory_transformer/test_modeling_trajectory_transformer.py` | 691 | 10,559 |
| `transformers/tests/models/transfo_xl/__init__.py` | 0 | 0 |
| `transformers/tests/models/transfo_xl/test_modeling_tf_transfo_xl.py` | 965 | 12,060 |
| `transformers/tests/models/transfo_xl/test_modeling_transfo_xl.py` | 1,726 | 23,198 |
| `transformers/tests/models/transfo_xl/test_tokenization_transfo_xl.py` | 346 | 4,121 |
| `transformers/tests/models/trocr/__init__.py` | 0 | 0 |
| `transformers/tests/models/trocr/test_modeling_trocr.py` | 511 | 7,014 |
| `transformers/tests/models/unispeech/__init__.py` | 0 | 0 |
| `transformers/tests/models/unispeech/test_modeling_unispeech.py` | 1,483 | 22,758 |
| `transformers/tests/models/unispeech_sat/__init__.py` | 0 | 0 |
| `transformers/tests/models/unispeech_sat/test_modeling_unispeech_sat.py` | 2,312 | 36,931 |
| `transformers/tests/models/van/__init__.py` | 0 | 0 |
| `transformers/tests/models/van/test_modeling_van.py` | 741 | 10,458 |
| `transformers/tests/models/vilt/__init__.py` | 0 | 0 |
| `transformers/tests/models/vilt/test_feature_extraction_vilt.py` | 660 | 9,792 |
| `transformers/tests/models/vilt/test_modeling_vilt.py` | 1,582 | 24,764 |
| `transformers/tests/models/vision_encoder_decoder/__init__.py` | 0 | 0 |
| `transformers/tests/models/vision_encoder_decoder/test_modeling_flax_vision_encoder_decoder.py` | 1,228 | 21,026 |
| `transformers/tests/models/vision_encoder_decoder/test_modeling_tf_vision_encoder_decoder.py` | 2,128 | 37,471 |
| `transformers/tests/models/vision_encoder_decoder/test_modeling_vision_encoder_decoder.py` | 1,815 | 32,484 |
| `transformers/tests/models/vision_text_dual_encoder/__init__.py` | 0 | 0 |
| `transformers/tests/models/vision_text_dual_encoder/test_modeling_flax_vision_text_dual_encoder.py` | 976 | 16,030 |
| `transformers/tests/models/vision_text_dual_encoder/test_modeling_vision_text_dual_encoder.py` | 1,254 | 21,529 |
| `transformers/tests/models/vision_text_dual_encoder/test_processor_vision_text_dual_encoder.py` | 481 | 6,876 |
| `transformers/tests/models/visual_bert/__init__.py` | 0 | 0 |
| `transformers/tests/models/visual_bert/test_modeling_visual_bert.py` | 1,610 | 28,468 |
| `transformers/tests/models/vit/__init__.py` | 0 | 0 |
| `transformers/tests/models/vit/test_feature_extraction_vit.py` | 414 | 6,654 |
| `transformers/tests/models/vit/test_modeling_flax_vit.py` | 537 | 7,633 |
| `transformers/tests/models/vit/test_modeling_tf_vit.py` | 684 | 9,411 |
| `transformers/tests/models/vit/test_modeling_vit.py` | 787 | 11,384 |
| `transformers/tests/models/vit_mae/__init__.py` | 0 | 0 |
| `transformers/tests/models/vit_mae/test_modeling_tf_vit_mae.py` | 1,559 | 20,769 |
| `transformers/tests/models/vit_mae/test_modeling_vit_mae.py` | 948 | 12,576 |
| `transformers/tests/models/wav2vec2/__init__.py` | 0 | 0 |
| `transformers/tests/models/wav2vec2/test_feature_extraction_wav2vec2.py` | 678 | 9,803 |
| `transformers/tests/models/wav2vec2/test_modeling_flax_wav2vec2.py` | 1,687 | 22,477 |
| `transformers/tests/models/wav2vec2/test_modeling_tf_wav2vec2.py` | 1,567 | 23,365 |
| `transformers/tests/models/wav2vec2/test_modeling_wav2vec2.py` | 4,497 | 66,001 |
| `transformers/tests/models/wav2vec2/test_processor_wav2vec2.py` | 400 | 5,801 |
| `transformers/tests/models/wav2vec2/test_tokenization_wav2vec2.py` | 3,326 | 37,971 |
| `transformers/tests/models/wav2vec2_conformer/__init__.py` | 0 | 0 |
| `transformers/tests/models/wav2vec2_conformer/test_modeling_wav2vec2_conformer.py` | 2,594 | 38,889 |
| `transformers/tests/models/wav2vec2_phoneme/__init__.py` | 0 | 0 |
| `transformers/tests/models/wav2vec2_phoneme/test_tokenization_wav2vec2_phoneme.py` | 1,869 | 20,067 |
| `transformers/tests/models/wav2vec2_with_lm/__init__.py` | 0 | 0 |
| `transformers/tests/models/wav2vec2_with_lm/test_processor_wav2vec2_with_lm.py` | 1,169 | 18,850 |
| `transformers/tests/models/wavlm/__init__.py` | 0 | 0 |
| `transformers/tests/models/wavlm/test_modeling_wavlm.py` | 1,595 | 23,726 |
| `transformers/tests/models/xglm/__init__.py` | 0 | 0 |
| `transformers/tests/models/xglm/test_modeling_flax_xglm.py` | 1,011 | 15,315 |
| `transformers/tests/models/xglm/test_modeling_xglm.py` | 1,569 | 24,470 |
| `transformers/tests/models/xglm/test_tokenization_xglm.py` | 894 | 8,378 |
| `transformers/tests/models/xlm/__init__.py` | 0 | 0 |
| `transformers/tests/models/xlm/test_modeling_tf_xlm.py` | 794 | 12,345 |
| `transformers/tests/models/xlm/test_modeling_xlm.py` | 1,058 | 17,438 |
| `transformers/tests/models/xlm/test_tokenization_xlm.py` | 297 | 3,293 |
| `transformers/tests/models/xlm_prophetnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/xlm_prophetnet/test_modeling_xlm_prophetnet.py` | 598 | 7,874 |
| `transformers/tests/models/xlm_prophetnet/test_tokenization_xlm_prophetnet.py` | 1,029 | 7,620 |
| `transformers/tests/models/xlm_roberta/__init__.py` | 0 | 0 |
| `transformers/tests/models/xlm_roberta/test_modeling_flax_xlm_roberta.py` | 200 | 1,889 |
| `transformers/tests/models/xlm_roberta/test_modeling_tf_xlm_roberta.py` | 205 | 2,028 |
| `transformers/tests/models/xlm_roberta/test_modeling_xlm_roberta.py` | 307 | 3,061 |
| `transformers/tests/models/xlm_roberta/test_tokenization_xlm_roberta.py` | 1,587 | 14,701 |
| `transformers/tests/models/xlm_roberta_xl/__init__.py` | 0 | 0 |
| `transformers/tests/models/xlm_roberta_xl/test_modeling_xlm_roberta_xl.py` | 1,264 | 20,812 |
| `transformers/tests/models/xlnet/__init__.py` | 0 | 0 |
| `transformers/tests/models/xlnet/test_modeling_tf_xlnet.py` | 1,840 | 21,563 |
| `transformers/tests/models/xlnet/test_modeling_xlnet.py` | 2,157 | 27,868 |
| `transformers/tests/models/xlnet/test_tokenization_xlnet.py` | 1,528 | 10,441 |
| `transformers/tests/models/yolos/__init__.py` | 0 | 0 |
| `transformers/tests/models/yolos/test_feature_extraction_yolos.py` | 938 | 14,166 |
| `transformers/tests/models/yolos/test_modeling_yolos.py` | 975 | 14,752 |
| `transformers/tests/models/yoso/__init__.py` | 0 | 0 |
| `transformers/tests/models/yoso/test_modeling_yoso.py` | 885 | 15,266 |
| `transformers/tests/onnx/__init__.py` | 0 | 0 |
| `transformers/tests/onnx/test_onnx.py` | 693 | 8,104 |
| `transformers/tests/onnx/test_onnx_v2.py` | 1,039 | 15,159 |
| `transformers/tests/optimization/__init__.py` | 0 | 0 |
| `transformers/tests/optimization/test_optimization.py` | 516 | 6,080 |
| `transformers/tests/optimization/test_optimization_tf.py` | 291 | 4,174 |
| `transformers/tests/pipelines/__init__.py` | 0 | 0 |
| `transformers/tests/pipelines/test_pipelines_audio_classification.py` | 344 | 4,140 |
| `transformers/tests/pipelines/test_pipelines_automatic_speech_recognition.py` | 2,665 | 35,188 |
| `transformers/tests/pipelines/test_pipelines_common.py` | 1,812 | 23,374 |
| `transformers/tests/pipelines/test_pipelines_conversational.py` | 1,183 | 17,154 |
| `transformers/tests/pipelines/test_pipelines_feature_extraction.py` | 1,224 | 10,295 |
| `transformers/tests/pipelines/test_pipelines_fill_mask.py` | 1,481 | 18,211 |
| `transformers/tests/pipelines/test_pipelines_image_classification.py` | 585 | 8,299 |
| `transformers/tests/pipelines/test_pipelines_image_segmentation.py` | 953 | 14,053 |
| `transformers/tests/pipelines/test_pipelines_object_detection.py` | 908 | 10,985 |
| `transformers/tests/pipelines/test_pipelines_question_answering.py` | 2,660 | 24,757 |
| `transformers/tests/pipelines/test_pipelines_summarization.py` | 966 | 8,730 |
| `transformers/tests/pipelines/test_pipelines_table_question_answering.py` | 2,625 | 30,354 |
| `transformers/tests/pipelines/test_pipelines_text2text_generation.py` | 370 | 4,877 |
| `transformers/tests/pipelines/test_pipelines_text_classification.py` | 597 | 7,143 |
| `transformers/tests/pipelines/test_pipelines_text_generation.py` | 724 | 8,952 |
| `transformers/tests/pipelines/test_pipelines_token_classification.py` | 2,471 | 32,409 |
| `transformers/tests/pipelines/test_pipelines_translation.py` | 526 | 7,203 |
| `transformers/tests/pipelines/test_pipelines_visual_question_answering.py` | 353 | 4,186 |
| `transformers/tests/pipelines/test_pipelines_zero_shot.py` | 1,458 | 15,292 |
| `transformers/tests/pipelines/test_pipelines_zero_shot_image_classification.py` | 785 | 9,135 |
| `transformers/tests/sagemaker/README.md` | 1,054 | 9,529 |
| `transformers/tests/sagemaker/__init__.py` | 9 | 110 |
| `transformers/tests/sagemaker/conftest.py` | 144 | 2,183 |
| `transformers/tests/sagemaker/scripts/pytorch/requirements.txt` | 15 | 155 |
| `transformers/tests/sagemaker/scripts/pytorch/run_ddp.py` | 120 | 1,468 |
| `transformers/tests/sagemaker/scripts/pytorch/run_glue_model_parallelism.py` | 2,295 | 23,782 |
| `transformers/tests/sagemaker/scripts/tensorflow/requirements.txt` | 14 | 140 |
| `transformers/tests/sagemaker/scripts/tensorflow/run_tf.py` | 263 | 3,690 |
| `transformers/tests/sagemaker/scripts/tensorflow/run_tf_dist.py` | 486 | 7,326 |
| `transformers/tests/sagemaker/test_multi_node_data_parallel.py` | 279 | 4,254 |
| `transformers/tests/sagemaker/test_multi_node_model_parallel.py` | 295 | 4,521 |
| `transformers/tests/sagemaker/test_single_node_gpu.py` | 230 | 3,554 |
| `transformers/tests/test_configuration_common.py` | 1,157 | 15,564 |
| `transformers/tests/test_feature_extraction_common.py` | 592 | 8,753 |
| `transformers/tests/test_modeling_common.py` | 9,402 | 134,040 |
| `transformers/tests/test_modeling_flax_common.py` | 3,890 | 53,118 |
| `transformers/tests/test_modeling_tf_common.py` | 6,668 | 97,660 |
| `transformers/tests/test_sequence_feature_extraction_common.py` | 1,112 | 18,048 |
| `transformers/tests/test_tokenization_common.py` | 12,865 | 205,638 |
| `transformers/tests/tokenization/__init__.py` | 0 | 0 |
| `transformers/tests/tokenization/test_tokenization_fast.py` | 704 | 8,606 |
| `transformers/tests/tokenization/test_tokenization_utils.py` | 853 | 13,001 |
| `transformers/tests/trainer/__init__.py` | 0 | 0 |
| `transformers/tests/trainer/test_data_collator.py` | 2,778 | 41,956 |
| `transformers/tests/trainer/test_trainer.py` | 7,504 | 102,536 |
| `transformers/tests/trainer/test_trainer_callback.py` | 699 | 10,185 |
| `transformers/tests/trainer/test_trainer_distributed.py` | 455 | 5,060 |
| `transformers/tests/trainer/test_trainer_seq2seq.py` | 351 | 4,854 |
| `transformers/tests/trainer/test_trainer_tpu.py` | 394 | 4,020 |
| `transformers/tests/trainer/test_trainer_utils.py` | 1,784 | 21,750 |
| `transformers/tests/utils/__init__.py` | 0 | 0 |
| `transformers/tests/utils/test_activations.py` | 200 | 2,269 |
| `transformers/tests/utils/test_activations_tf.py` | 184 | 1,992 |
| `transformers/tests/utils/test_add_new_model_like.py` | 2,981 | 51,104 |
| `transformers/tests/utils/test_cli.py` | 185 | 1,840 |
| `transformers/tests/utils/test_convert_slow_tokenizer.py` | 83 | 1,364 |
| `transformers/tests/utils/test_doc_samples.py` | 409 | 4,407 |
| `transformers/tests/utils/test_file_utils.py` | 739 | 9,347 |
| `transformers/tests/utils/test_generic.py` | 173 | 2,107 |
| `transformers/tests/utils/test_hf_argparser.py` | 761 | 9,597 |
| `transformers/tests/utils/test_image_utils.py` | 1,742 | 21,895 |
| `transformers/tests/utils/test_logging.py` | 438 | 5,406 |
| `transformers/tests/utils/test_model_card.py` | 256 | 3,491 |
| `transformers/tests/utils/test_model_output.py` | 310 | 3,568 |
| `transformers/tests/utils/test_modeling_tf_core.py` | 941 | 15,214 |
| `transformers/tests/utils/test_offline.py` | 303 | 2,671 |
| `transformers/tests/utils/test_skip_decorators.py` | 435 | 3,519 |
| `transformers/tests/utils/test_utils_check_copies.py` | 908 | 11,356 |
| `transformers/tests/utils/test_versions_utils.py` | 306 | 3,480 |
| `transformers/utils/check_config_docstrings.py` | 301 | 3,081 |
| `transformers/utils/check_copies.py` | 2,155 | 22,306 |
| `transformers/utils/check_dummies.py` | 627 | 6,184 |
| `transformers/utils/check_inits.py` | 1,192 | 12,447 |
| `transformers/utils/check_repo.py` | 2,997 | 31,418 |
| `transformers/utils/check_table.py` | 986 | 9,810 |
| `transformers/utils/check_tf_ops.py` | 409 | 3,574 |
| `transformers/utils/custom_init_isort.py` | 1,179 | 10,274 |
| `transformers/utils/documentation_tests.txt` | 77 | 3,927 |
| `transformers/utils/download_glue_data.py` | 544 | 8,285 |
| `transformers/utils/get_modified_files.py` | 207 | 1,482 |
| `transformers/utils/notification_service.py` | 2,448 | 31,075 |
| `transformers/utils/notification_service_doc_tests.py` | 1,132 | 12,870 |
| `transformers/utils/prepare_for_doc_test.py` | 561 | 4,701 |
| `transformers/utils/print_env.py` | 186 | 1,723 |
| `transformers/utils/release.py` | 617 | 6,210 |
| `transformers/utils/sort_auto_mappings.py` | 354 | 3,312 |
| `transformers/utils/test_module/__init__.py` | 0 | 0 |
| `transformers/utils/test_module/custom_configuration.py` | 29 | 380 |
| `transformers/utils/test_module/custom_feature_extraction.py` | 7 | 117 |
| `transformers/utils/test_module/custom_modeling.py` | 55 | 772 |
| `transformers/utils/test_module/custom_processing.py` | 12 | 172 |
| `transformers/utils/test_module/custom_tokenization.py` | 7 | 88 |
| `transformers/utils/test_module/custom_tokenization_fast.py` | 14 | 193 |
| `transformers/utils/tests_fetcher.py` | 2,694 | 28,492 |
| `transformers/utils/tf_ops/onnx.json` | 259 | 6,060 |
| `transformers/utils/update_metadata.py` | 833 | 10,573 |
| `transformers/valohai.yaml` | 291 | 3,237 |
| `tsnejs/.DS_Store` | — | 6,148 |
| `tsnejs/Readme.md` | 354 | 2,496 |
| `tsnejs/tsne.js` | 1,644 | 11,292 |
| `ulogme/.gitignore` | 8 | 68 |
| `ulogme/README.md` | 1,108 | 6,995 |
| `ulogme/export_events.py` | 441 | 3,165 |
| `ulogme/keyfreq.sh` | 105 | 708 |
| `ulogme/legacy_split_events.py` | 481 | 3,013 |
| `ulogme/logactivewin.sh` | 341 | 2,494 |
| `ulogme/logdesktop.sh` | 81 | 615 |
| `ulogme/note.sh` | 64 | 370 |
| `ulogme/osx/.gitignore` | 1 | 7 |
| `ulogme/osx/build_app.sh` | 6 | 35 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Frameworks/Python.framework/Versions/2.7/Python` | — | 2,564,496 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Frameworks/Python.framework/Versions/2.7/Resources/Info.plist` | 42 | 873 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Frameworks/Python.framework/Versions/2.7/include/python2.7/pyconfig.h` | 6,179 | 36,733 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/Makefile` | 4,921 | 49,702 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Info.plist` | 120 | 2,453 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/MacOS/python` | — | 58,288 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/MacOS/ulogme_osx` | — | 71,316 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/PkgInfo` | 1 | 8 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/PythonApplet.icns` | — | 63,136 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/__boot__.py` | 868 | 10,443 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/__error__.sh` | 89 | 559 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/include/python2.7/pyconfig.h` | 6,179 | 36,733 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/config/Makefile` | 4,921 | 49,702 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/config/Setup` | 2,783 | 18,484 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/config/Setup.config` | 59 | 368 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/config/Setup.local` | 8 | 41 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/__init__.py` | 294 | 2,856 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/__init__.pyo` | — | 3,172 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/_parseaddr.py` | 1,692 | 15,733 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/_parseaddr.pyo` | — | 15,175 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/base64mime.py` | 798 | 5,794 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/base64mime.pyo` | — | 5,573 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/charset.py` | 1,808 | 16,043 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/charset.pyo` | — | 14,343 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/encoders.py` | 217 | 2,015 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/encoders.pyo` | — | 2,582 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/errors.py` | 169 | 1,628 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/errors.pyo` | — | 4,279 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/feedparser.py` | 2,062 | 20,606 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/feedparser.pyo` | — | 12,201 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/generator.py` | 1,661 | 14,228 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/generator.pyo` | — | 11,335 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/header.py` | 2,748 | 22,243 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/header.pyo` | — | 14,392 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/iterators.py` | 257 | 2,202 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/iterators.pyo` | — | 2,616 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/message.py` | 3,534 | 30,720 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/message.pyo` | — | 30,973 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/__init__.py` | 1 | 2 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/__init__.pyo` | — | 180 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/application.py` | 126 | 1,256 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/application.pyo` | — | 1,734 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/audio.py` | 323 | 2,683 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/audio.pyo` | — | 3,109 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/base.py` | 83 | 794 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/base.pyo` | — | 1,266 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/image.py` | 202 | 1,764 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/image.pyo` | — | 2,199 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/message.py` | 152 | 1,286 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/message.pyo` | — | 1,598 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/multipart.py` | 180 | 1,573 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/multipart.pyo` | — | 1,819 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/nonmultipart.py` | 80 | 689 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/nonmultipart.pyo` | — | 1,036 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/text.py` | 104 | 1,006 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/mime/text.pyo` | — | 1,458 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/parser.py` | 379 | 3,300 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/parser.pyo` | — | 4,229 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/quoprimime.py` | 1,464 | 10,848 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/quoprimime.pyo` | — | 9,500 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/__init__.py` | 1 | 2 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/__init__.pyo` | — | 180 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/PyBanner048.gif` | — | 954 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/audiotest.au` | — | 24,544 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_01.txt` | 56 | 459 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_02.txt` | 308 | 2,811 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_03.txt` | 49 | 366 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_04.txt` | 104 | 961 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_05.txt` | 38 | 558 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_06.txt` | 103 | 1,037 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_07.txt` | 108 | 5,227 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_08.txt` | 39 | 452 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_09.txt` | 38 | 430 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_10.txt` | 71 | 882 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_11.txt` | 19 | 142 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_12.txt` | 52 | 642 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_12a.txt` | 52 | 644 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_13.txt` | 120 | 5,367 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_14.txt` | 88 | 641 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_15.txt` | 107 | 1,396 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_16.txt` | 438 | 5,203 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_17.txt` | 40 | 330 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_18.txt` | 13 | 230 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_19.txt` | 102 | 757 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_20.txt` | 62 | 507 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_21.txt` | 34 | 376 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_22.txt` | 80 | 1,894 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_23.txt` | 12 | 139 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_24.txt` | 14 | 157 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_25.txt` | 469 | 5,122 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_26.txt` | 131 | 2,099 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_27.txt` | 51 | 578 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_28.txt` | 36 | 380 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_29.txt` | 60 | 583 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_30.txt` | 32 | 322 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_31.txt` | 18 | 200 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_32.txt` | 40 | 418 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_33.txt` | 56 | 750 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_34.txt` | 38 | 300 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_35.txt` | 17 | 136 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_36.txt` | 53 | 816 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_37.txt` | 20 | 209 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_38.txt` | 232 | 2,548 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_39.txt` | 131 | 1,955 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_40.txt` | 12 | 197 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_41.txt` | 22 | 185 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_42.txt` | 29 | 313 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_43.txt` | 933 | 9,166 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_44.txt` | 100 | 895 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_45.txt` | 102 | 965 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/data/msg_46.txt` | 81 | 816 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email.py` | 9,677 | 130,364 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email.pyo` | — | 158,505 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_codecs.py` | 246 | 2,842 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_codecs.pyo` | — | 3,182 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_codecs_renamed.py` | 246 | 2,842 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_codecs_renamed.pyo` | — | 3,230 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_renamed.py` | 8,934 | 121,318 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_renamed.pyo` | — | 149,934 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_torture.py` | 307 | 3,669 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/test/test_email_torture.pyo` | — | 4,967 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/utils.py` | 1,173 | 9,863 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/email/utils.pyo` | — | 9,963 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/AppKit/_AppKit.so` | — | 71,248 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/AppKit/_inlines.so` | — | 38,624 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/CoreFoundation/_CoreFoundation.so` | — | 110,704 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/CoreFoundation/_inlines.so` | — | 46,576 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Foundation/_Foundation.so` | — | 110,256 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Foundation/_inlines.so` | — | 54,496 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/MacOS.so` | — | 50,800 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Nav.so` | — | 26,416 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreGraphics/_callbacks.so` | — | 75,424 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreGraphics/_coregraphics.so` | — | 53,296 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreGraphics/_doubleindirect.so` | — | 40,080 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreGraphics/_inlines.so` | — | 38,544 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreGraphics/_sortandmap.so` | — | 44,368 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/Quartz/CoreVideo/_CVPixelBuffer.so` | — | 40,176 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_AE.so` | — | 69,056 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Ctl.so` | — | 113,024 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Dlg.so` | — | 53,296 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Evt.so` | — | 40,944 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_File.so` | — | 92,592 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Menu.so` | — | 74,656 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Qd.so` | — | 34,368 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Res.so` | — | 65,968 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_Win.so` | — | 51,376 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_bisect.so` | — | 35,024 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_cn.so` | — | 277,440 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_hk.so` | — | 306,400 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_iso2022.so` | — | 51,760 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_jp.so` | — | 482,992 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_kr.so` | — | 265,056 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_codecs_tw.so` | — | 219,904 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_collections.so` | — | 63,264 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_ctypes.so` | — | 196,704 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_functools.so` | — | 40,176 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_hashlib.so` | — | 49,056 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_heapq.so` | — | 51,872 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_io.so` | — | 241,216 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_locale.so` | — | 44,768 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_multibytecodec.so` | — | 70,928 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_random.so` | — | 44,560 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_scproxy.so` | — | 40,976 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_socket.so` | — | 140,608 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_ssl.so` | — | 75,328 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_struct.so` | — | 76,016 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/_testcapi.so` | — | 94,960 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/array.so` | — | 84,768 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/audioop.so` | — | 60,544 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/binascii.so` | — | 52,144 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/bz2.so` | — | 75,920 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/cPickle.so` | — | 137,840 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/cStringIO.so` | — | 48,928 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/datetime.so` | — | 144,096 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/fcntl.so` | — | 43,952 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/gestalt.so` | — | 34,768 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/grp.so` | — | 35,424 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/itertools.so` | — | 99,968 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/math.so` | — | 70,592 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/objc/_objc.so` | — | 696,640 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/operator.so` | — | 72,624 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/parser.so` | — | 99,280 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/pyexpat.so` | — | 96,064 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/resource.so` | — | 43,952 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/select.so` | — | 61,920 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/strop.so` | — | 73,536 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/termios.so` | — | 48,496 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/time.so` | — | 57,872 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/unicodedata.so` | — | 1,395,808 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/lib-dynload/zlib.so` | — | 61,232 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/lib/python2.7/site-packages.zip` | — | 2,529,204 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/site.pyc` | — | 3,343 |
| `ulogme/osx/dist/ulogme_osx.app/Contents/Resources/ulogme_osx.py` | 542 | 6,490 |
| `ulogme/osx/osx_setup.sh` | 44 | 301 |
| `ulogme/osx/rewind7am.py` | 129 | 912 |
| `ulogme/osx/run_ulogme_osx.sh` | 191 | 1,519 |
| `ulogme/osx/setup.py` | 10 | 129 |
| `ulogme/osx/ulogme_osx.py` | 542 | 6,490 |
| `ulogme/render/.gitignore` | 2 | 36 |
| `ulogme/render/d3.min.js` | 2,806 | 146,658 |
| `ulogme/render/d3utils.js` | 443 | 3,704 |
| `ulogme/render/font_lato.css` | 45 | 655 |
| `ulogme/render/index.html` | 1,867 | 19,444 |
| `ulogme/render/index_style.css` | 448 | 3,532 |
| `ulogme/render/jquery-1.8.3.min.js` | 1,245 | 93,636 |
| `ulogme/render/overview.html` | 1,701 | 16,195 |
| `ulogme/render/overview_style.css` | 173 | 1,328 |
| `ulogme/render/render_settings_example.js` | 482 | 3,161 |
| `ulogme/render/render_utils.js` | 179 | 1,248 |
| `ulogme/render/spin.min.js` | 79 | 4,143 |
| `ulogme/render/ulogme_common.js` | 862 | 6,629 |
| `ulogme/render/underscore.min.js` | 361 | 14,682 |
| `ulogme/rewind7am.py` | 129 | 912 |
| `ulogme/ulogme.sh` | 27 | 178 |
| `ulogme/ulogme_serve.py` | 234 | 2,184 |

## Failures

| Target | Reason | Error |
| --- | --- | --- |
| `karpathy/Arxiv-Sanity` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/Deep-Q-Learning` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/Deep-Q-Learning/' |
| `karpathy/MatlabScripts` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/MatlabWrappers` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/MatlabWrappers/' |
| `karpathy/Random-Forest` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/Random-Forest/' |
| `karpathy/agents` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/alexnet` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/arxiv-bot` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/arxiv-sanity` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/arxiv-sanity/' |
| `karpathy/atari` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/atari/' |
| `karpathy/autograd` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/autograd/' |
| `karpathy/awesome` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/awesome/' |
| `karpathy/bigram` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/bigram/' |
| `karpathy/bio` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/blog` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/blog/' |
| `karpathy/caffe` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/caffe/' |
| `karpathy/calorie-ninja` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/cifar10` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/cifar10/' |
| `karpathy/convnet-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/cs231n` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/cs231n/' |
| `karpathy/cs231n.github.io` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/cs231n.github.io/' |
| `karpathy/cursor-tutor` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/cursor-tutor/' |
| `karpathy/cvpr` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/deep-learning-papers` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/deep-learning-school` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/deep-learning-school/' |
| `karpathy/deepdream` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/deepdream/' |
| `karpathy/deepspeech` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/deepspeech/' |
| `karpathy/diffusion` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/diffusion/' |
| `karpathy/digit` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/digit/' |
| `karpathy/dinosaur` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/dinosaur/' |
| `karpathy/dotfiles` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/dotfiles/' |
| `karpathy/dqn` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/dqn/' |
| `karpathy/dqn-tensorflow` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/emoji` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/eureka` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/experiments` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/experiments/' |
| `karpathy/forest-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/fun` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/fun/' |
| `karpathy/gan` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/gan/' |
| `karpathy/googlenet` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/gpt` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/gpt/' |
| `karpathy/gpt-2` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/gpt-2/' |
| `karpathy/grad-cam` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/grad-cam/' |
| `karpathy/gradcheck` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/gradcheck/' |
| `karpathy/gridworld` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/gym` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/gym/' |
| `karpathy/hbase` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/iccv` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/icml` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/image-captioning` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/image-captioning/' |
| `karpathy/imagenet` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/imagenet/' |
| `karpathy/ipython-notebooks` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/ipython-notebooks/' |
| `karpathy/llama` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/llama/' |
| `karpathy/llama.cpp` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/llamafile` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/llamafile/' |
| `karpathy/llm-viz` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/llm.c-cuda` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/llmc` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/llms` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/lstm` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/lstm/' |
| `karpathy/lstm-char-cnn` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/magicarp` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/magicarp/' |
| `karpathy/makemore-rs` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/mathquiz` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/matlab` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/micrograd-cpp` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/micrograd-rs` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/micrograd-rs/' |
| `karpathy/mingpt-demo` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/mingpt-demo/' |
| `karpathy/mini-llm` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/mini-llm/' |
| `karpathy/minsearch` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/minsearch/' |
| `karpathy/ml-notes` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/mnist` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/mnist/' |
| `karpathy/modded-nanogpt` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/modded-nanogpt/' |
| `karpathy/mywiki` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/mywiki/' |
| `karpathy/nano-llama31` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nano-llama31/' |
| `karpathy/nanoGPT-lecture` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanoGPT-lecture/' |
| `karpathy/nanoGPT-llama` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanoGPT-mup` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanoGPT2` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanoRL` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanoRL/' |
| `karpathy/nanoVLM` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanoVLM/' |
| `karpathy/nanoagent` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanodiffusion` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanoeval` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanoeval/' |
| `karpathy/nanoflow` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanoflow/' |
| `karpathy/nanogpt-mlx` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/nanogpt-speedrun` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanogpt-speedrun/' |
| `karpathy/nanogpt.c` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanogpt.c/' |
| `karpathy/nanogrpo` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/nanogrpo/' |
| `karpathy/nanot5` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/neural-networks` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/neural-networks/' |
| `karpathy/neural-style` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/neural-style/' |
| `karpathy/neural-vqa` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/neural-vqa/' |
| `karpathy/neuraltalk2.torch` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/neuraltalk3` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/neuraltalk3/' |
| `karpathy/nips` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/notebooks` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/notebooks/' |
| `karpathy/notpron` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/notpron/' |
| `karpathy/numpy-tutorial` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/numpy-tutorial/' |
| `karpathy/openai-gym` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/openai-gym/' |
| `karpathy/pixelcnn` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pixelcnn/' |
| `karpathy/playground` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/playground/' |
| `karpathy/policy-gradient` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/policy-gradient/' |
| `karpathy/pong` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pong/' |
| `karpathy/puckworld` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-cnn` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-examples` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pytorch-examples/' |
| `karpathy/pytorch-gan` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-lightning` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pytorch-lightning/' |
| `karpathy/pytorch-quantization` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pytorch-quantization/' |
| `karpathy/pytorch-rl` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-transformer` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-tutorial` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pytorch-tutorial/' |
| `karpathy/pytorch-vae` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/pytorch-vq-vae` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/pytorch-vq-vae/' |
| `karpathy/recurrent-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/reinforce` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/reinforce/' |
| `karpathy/reinforce-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/resnet` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/rl` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/rlgames` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/rnn` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/rnn/' |
| `karpathy/sanity` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/sanity/' |
| `karpathy/scripts` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/scripts/' |
| `karpathy/sketch-rnn` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/sketch-rnn/' |
| `karpathy/sortfix` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/sortfix/' |
| `karpathy/sortfix-demo` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/sortfixdemo` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/starter-code` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/starter-code/' |
| `karpathy/svm-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/talks` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/talks/' |
| `karpathy/tensorflow` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/tiny-shakespeare` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/tiny-shakespeare/' |
| `karpathy/tinyshakespeare` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/tinyshakespeare/' |
| `karpathy/torch` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/torch-rnn` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/torch-rnn/' |
| `karpathy/torch7` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/tsne` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/tsne/' |
| `karpathy/tsne-js` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/tsne-pytorch` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/tsne-pytorch/' |
| `karpathy/tsne-viz` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/tsne-viz/' |
| `karpathy/ttmik` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/ttmik/' |
| `karpathy/tweetnlp` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/twitter-bot` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/twitter-sentiment` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/twitter-sentiment/' |
| `karpathy/vae` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/vae/' |
| `karpathy/vgg` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/vision` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/vision/' |
| `karpathy/vq-vae` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/vq-vae/' |
| `karpathy/waterworld` | repo not found or not public | git ls-remote exited non-zero; GitHub returns an auth challenge for repos that do not exist or are not public |
| `karpathy/wavenet` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/wavenet/' |
| `karpathy/whisper` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/whisper/' |
| `karpathy/word2vec` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/word2vec/' |
| `karpathy/zero-to-hero` | repo not found or not public | fatal: Authentication failed for 'https://github.com/karpathy/zero-to-hero/' |
