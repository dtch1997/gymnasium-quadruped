import numpy as np
from dm_control import suite, viewer

import gymnasium_quadruped.envs  # noqa: F401

# Load one task:
env = suite.load(domain_name="a1_dmc", task_name="walk")
action_spec = env.action_spec()

# Define a uniform random policy.
def random_policy(time_step):
    del time_step  # Unused.
    return np.random.uniform(low=action_spec.minimum, high=action_spec.maximum, size=action_spec.shape)


viewer.launch(env, policy=random_policy)
