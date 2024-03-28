import argparse
import random
import time


class FollowerSimulator:
    """
    Class to simulate follower growth on a social network.
    """

    EVENTS = {
        # Probability of each event, message and its impact on the follower count (from,to)
        (1, 2): ("You post a viral post! 🚀", (200, 300)),
        (6, 10): ("Uh-oh! A controversial post. 😬", (-60, -40)),
        (11, 13): ("It's a holiday! Extra followers! 🎄🎊", (20, 40)),
        (14, 16): ("You got mentioned by a celebrity! 🌟", (100, 200)),
        (17, 20): ("You took a social media break. 😴", (-20, -10)),
        (21, 22): ("You sponsored a post! 💰", (500, 1000))
    }

    MIN_EVENT = 1
    MAX_EVENT = 100
    SLEEP_TIME = 0.5

    def __init__(self, initial_followers: int, random_range_start: int, random_range_end: int) -> None:
        """
        Initialize the FollowerSimulator object.

        Args:
            initial_followers: The initial number of followers.
            random_range_start: The starting value of the random follower growth.
            random_range_end: The ending value of the random follower growth.
        """
        self.initial_followers = initial_followers
        self.current_followers = self.initial_followers
        self.total_new_followers: int = 0
        self.total_event_followers: int = 0
        self.cycles: int = 0
        self.random_range_start = random_range_start
        self.random_range_end = random_range_end
        self.current_line: str = ""

    def simulate_cycle(self) -> None:
        """
        Simulate a single cycle of follower growth.
        """
        new_followers = random.randint(self.random_range_start, self.random_range_end)
        event_followers: int = 0
        event_followers += self.random_event_effect()
        new_followers += event_followers
        self.current_followers += new_followers
        self.total_new_followers += new_followers
        self.total_event_followers += event_followers
        self.cycles += 1

        self.current_line = f"New: {new_followers}, By events: {self.total_event_followers}, Total: {self.current_followers}{' ' * 10}"
        print('\r\033[K' + self.current_line, end='\r')

    def random_event_effect(self) -> int:
        """
        Generate a random event with an impact on the follower count.

        Returns:
            The number of followers gained or lost due to the event.
        """
        event: int = random.randint(self.MIN_EVENT, self.MAX_EVENT)
        for event_range, (message, follower_range) in self.EVENTS.items():
            if event in range(*event_range):
                event_followers = random.randint(*follower_range)
                print(f"{message} -> {event_followers}{' ' * 20}")
                return event_followers
        return 0

    def summary(self) -> None:
        """
        Print a summary of the simulation. Shows the number of cycles, initial followers, total new followers,
        total event followers, percentage of new followers gained by events, and the final number of followers.
        If the simulation is interrupted by the user, the current line is cleared.
        """
        event_percentage: str = f"{self.total_event_followers/self.total_new_followers*100:.2f}"
        print("\n\n-------- Simulation Summary --------")
        print(f"Simulation cycles........: {self.cycles}")
        print(f"Initial followers........: {self.initial_followers}")
        print(f"Total new followers......: {self.total_new_followers}")
        print(f"Total event followers....: {self.total_event_followers}")
        print(f"Percentage by events.....: {event_percentage}%")
        print(f"Final number of followers: {self.current_followers}\n")


def main() -> None:
    """
    Main function to run the follower growth simulation.
    """
    parser = argparse.ArgumentParser(description="Simulate social network follower growth.")
    parser.add_argument("initial_followers", type=int,
                        help="Initial number of followers")
    parser.add_argument("random_range_start", type=int,
                        help="Starting value of random follower growth")
    parser.add_argument("random_range_end", type=int,
                        help="Ending value of random follower growth")
    parser.add_argument("-c", "--cycles", type=int, default=None,
                        help="Number of cycles to run before exiting (optional)")
    args = parser.parse_args()

    if args.random_range_start > args.random_range_end:
        print("Error: The starting value of the random range must be less than or equal to the ending value.")
        exit(1)

    simulator = FollowerSimulator(args.initial_followers, args.random_range_start, args.random_range_end)
    print(f'Starting with {args.initial_followers} followers.')

    try:
        while args.cycles is None or simulator.cycles < args.cycles:
            simulator.simulate_cycle()
            time.sleep(FollowerSimulator.SLEEP_TIME)
    except KeyboardInterrupt:
        print(f"\r\033[K{simulator.current_line}")
    finally:
        simulator.summary()


if __name__ == "__main__":
    main()
