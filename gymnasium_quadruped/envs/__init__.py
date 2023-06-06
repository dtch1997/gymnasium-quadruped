from gymnasium.envs.registration import (
    register,
)

register(
    id="MyAnt-v4",
    entry_point="quadruped_bc.envs.ant:AntEnv",
    max_episode_steps=1000,
    reward_threshold=6000.0,
)

register(
    id="A1-v4",
    entry_point="quadruped_bc.envs.a1:A1Env",
    max_episode_steps=1000,
    reward_threshold=6000.0,
)
