import unittest

from gymnasium_quadruped.envs.a1 import A1Env


class A1EnvTestCase(unittest.TestCase):
    def setUp(self):
        self.env = A1Env()

    def tearDown(self):
        self.env.close()

    def test_step_returns_valid_results(self):
        _, _ = self.env.reset()
        action = self.env.action_space.sample()
        next_observation, reward, terminated, truncated, info = self.env.step(action)

        self.assertIsNotNone(next_observation)
        self.assertIsNotNone(reward)
        self.assertIsNotNone(terminated)
        self.assertIsNotNone(truncated)
        self.assertIsNotNone(info)

    def test_reset_returns_valid_observation(self):
        observation, info = self.env.reset()
        self.assertIsNotNone(observation)
        self.assertIsNotNone(info)
        self.assertEqual(observation.shape, self.env.observation_space.shape)


if __name__ == "__main__":
    unittest.main()
