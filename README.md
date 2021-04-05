## TransGanFormer (wip)

Implementation of TransGanFormer, an all-attention GAN that combines the finding from the recent <a href="https://arxiv.org/abs/2103.01209">GansFormer</a> and <a href="https://arxiv.org/abs/2102.07074">TransGan</a> paper. It will also contain a bunch of tricks I have picked up building transformers and GANs for the last year or so, including efficient linear attention and pixel level attention.

## Install

```bash
$ pip install transganformer
```

## Usage

```bash
$ transganformer --data ./path/to/data
```

## Citations

```bibtex
@misc{jiang2021transgan,
    title   = {TransGAN: Two Transformers Can Make One Strong GAN}, 
    author  = {Yifan Jiang and Shiyu Chang and Zhangyang Wang},
    year    = {2021},
    eprint  = {2102.07074},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}
```

```bibtex
@misc{hudson2021generative,
    title   = {Generative Adversarial Transformers}, 
    author  = {Drew A. Hudson and C. Lawrence Zitnick},
    year    = {2021},
    eprint  = {2103.01209},
    archivePrefix = {arXiv},
    primaryClass = {cs.CV}
}
```
