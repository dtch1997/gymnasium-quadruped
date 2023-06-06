import gymnasium as gym


def test_my_ant_env():
    gym.make("MyAnt-v4")


def test_quadruped_env():
    gym.make("A1-v4")
