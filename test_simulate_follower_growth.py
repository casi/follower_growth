import unittest
from unittest.mock import call, patch

from simulate_follower_growth import FollowerSimulator


class TestFollowerSimulator(unittest.TestCase):

    def setUp(self):
        self.simulator = FollowerSimulator(100, 5, 10)

    def test_initial_conditions(self):
        self.assertEqual(self.simulator.initial_followers, 100)
        self.assertEqual(self.simulator.current_followers, 100)
        self.assertEqual(self.simulator.total_new_followers, 0)
        self.assertEqual(self.simulator.cycles, 0)
        self.assertEqual(self.simulator.random_range_start, 5)
        self.assertEqual(self.simulator.random_range_end, 10)

    @patch('builtins.print')
    def test_simulate_cycle(self, mock_print):
        self.assertEqual(self.simulator.current_followers, 100)
        self.simulator.simulate_cycle()
        self.assertEqual(self.simulator.cycles, 1)
        self.assertNotEqual(self.simulator.current_followers, 100)

    @patch('random.randint')
    @patch('builtins.print')
    def test_random_event_effect(self, mock_print, mock_randint):
        mock_randint.side_effect = [12, 100]  # Event: "It's a holiday! Extra followers! 🎄🎊"
        bonus_followers = self.simulator.random_event_effect()
        mock_print.assert_called_with("It's a holiday! Extra followers! 🎄🎊 -> 100                    ")
        self.assertFalse(20 <= bonus_followers <= 40)

    @patch('builtins.print')
    def test_summary(self, moch_print):
        self.simulator.simulate_cycle()
        with patch('builtins.print') as mock_print:
            self.simulator.summary()
            calls = [call("\n\n-------- Simulation Summary --------"),
                    call(f"Simulation cycles........: {self.simulator.cycles}"),
                    call(f"Initial followers........: {self.simulator.initial_followers}"),
                    call(f"Total new followers......: {self.simulator.total_new_followers}"),
                    call(f"Total event followers....: {self.simulator.total_event_followers}"),
                    call(f"Percentage by events.....: {self.simulator.total_event_followers / self.simulator.total_new_followers * 100:.2f}%"),
                    call(f"Final number of followers: {self.simulator.current_followers}\n")]
            mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
