import unittest
from unittest.mock import patch

from mock import call

from simulate_follower_growth import FollowerSimulator


class TestFollowerSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = FollowerSimulator(100, 5, 10)

    def test_initial_conditions(self):
        self.assertEqual(self.simulator.current_followers, 100)
        self.assertEqual(self.simulator.total_new_followers, 0)
        self.assertEqual(self.simulator.cycles, 0)
        self.assertEqual(self.simulator.random_range_start, 5)
        self.assertEqual(self.simulator.random_range_end, 10)

    @patch('random.randint')
    @patch('builtins.print')
    def test_random_event_effect(self, mock_print, mock_randint):
        mock_randint.return_value = 12  # Event: "It's a holiday! Extra followers! 🎄🎊"
        bonus_followers = self.simulator.random_event_effect()
        mock_print.assert_called_with("It's a holiday! Extra followers! 🎄🎊")
        self.assertFalse(20 <= bonus_followers <= 40) 

    def test_summary(self):
        with patch('builtins.print') as mock_print:
            self.simulator.summary()
            calls = [call("\n--- Simulation Summary ---"),
                     call(f"Simulation cycles: {self.simulator.cycles}"),
                     call(f"Initial followers: {self.simulator.current_followers - self.simulator.total_new_followers}"),
                     call(f"Total new followers: {self.simulator.total_new_followers}"),
                     call(f"Final number of followers: {self.simulator.current_followers}\n")]
            mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
