from dm_control.suite import _DOMAINS
from gymnasium.envs.registration import (
    register,
)

from gymnasium_quadruped.envs import a1_dmc

register(
    id="MyAnt-v4",
    entry_point="gymnasium_quadruped.envs.ant:AntEnv",
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id="A1-v4",
    entry_point="gymnasium_quadruped.envs.a1:A1Env",
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

_DOMAINS["a1_dmc"] = a1_dmc
