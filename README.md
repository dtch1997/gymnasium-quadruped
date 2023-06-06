# gymnasium-quadruped

[![Release](https://img.shields.io/github/v/release/dtch1997/gymnasium-quadruped)](https://img.shields.io/github/v/release/dtch1997/gymnasium-quadruped)
[![Build status](https://img.shields.io/github/actions/workflow/status/dtch1997/gymnasium-quadruped/main.yml?branch=main)](https://github.com/dtch1997/gymnasium-quadruped/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/dtch1997/gymnasium-quadruped/branch/main/graph/badge.svg)](https://codecov.io/gh/dtch1997/gymnasium-quadruped)
[![Commit activity](https://img.shields.io/github/commit-activity/m/dtch1997/gymnasium-quadruped)](https://img.shields.io/github/commit-activity/m/dtch1997/gymnasium-quadruped)
[![License](https://img.shields.io/github/license/dtch1997/gymnasium-quadruped)](https://img.shields.io/github/license/dtch1997/gymnasium-quadruped)

Gymnasium environment for training quadruped legged robots

- **Github repository**: <https://github.com/dtch1997/gymnasium-quadruped/>
- **Documentation** <https://dtch1997.github.io/gymnasium-quadruped/>

## Getting started

Install the environment and the pre-commit hooks with 

```bash
make install
```

## Learning

This repository contains a simple PPO implementation in `learning/ppo.py`, adapted from [CleanRL](https://github.com/vwxyzjn/cleanrl).

To install learning-related dependencies, run:
```bash
poetry install --with learning
```

## Contributing 

We welcome contributions; please refer to the [guidelines](CONTRIBUTING.rst)

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).