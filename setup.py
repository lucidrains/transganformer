import sys
from setuptools import setup, find_packages

sys.path[0:0] = ['transganformer']
from version import __version__

setup(
  name = 'transganformer',
  packages = find_packages(),
  entry_points={
    'console_scripts': [
      'transganformer = transganformer.cli:main',
    ],
  },
  version = __version__,
  license='MIT',
  description = 'TransGanFormer',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/transganformer',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'generative adversarial networks',
    'transformers',
    'attention-mechanism'
  ],
  install_requires=[
    'einops>=0.3',
    'fire',
    'kornia',
    'numpy',
    'pillow',
    'retry',
    'torch>=1.6',
    'torchvision',
    'tqdm'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)