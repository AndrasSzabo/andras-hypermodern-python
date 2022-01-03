# andras-hypermodern-python

[![Tests](https://github.com/AndrasSzabo/andras-hypermodern-python/workflows/Tests/badge.svg)](https://github.com/AndrasSzabo/andras-hypermodern-python/actions?workflow=Tests)

A repo following the excellent article here:
https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769


## Setup

To install pyenv correctly on Ubuntu 20.04, slight differences were needed compared with the article. The part required in `~/.bashrc` is:

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

Installing poetry following the instructions on their GitHub project page:
```
curl -sSL https://install.python-poetry.org | python
```
