"""Example running TD-MPC on dm_control.

Run this example with

```shell
python -m cdrl.examples.tdmpc.main \
  --config cdrl/examples/tdmpc/configs/walker.py \
  --config.task=walker-walk
```

See configs/ for configurations for other environments.

"""
import functools
import os

from absl import app
from absl import flags
from absl import logging

os.environ["MUJOCO_GL"] = "egl"
# pylint: disable=wrong-import-position

import optax
import tensorflow as tf
from acme import wrappers
from acme.jax import experiments
from ml_collections import config_flags

from learning.tdmpc import tdmpc
from learning.utils import experiment_utils
