import gymnasium as gym
import numpy as np

from gymnasium_quadruped.envs.dm_wrapper import GymWrapper


def test_env():
    env = gym.make("A1-v4")
    env = GymWrapper(env)

    action_spec = env.action_spec()
    time_step = env.reset()
    while not time_step.last():
        action = np.random.uniform(action_spec.minimum, action_spec.maximum, size=action_spec.shape)
        time_step = env.step(action)
