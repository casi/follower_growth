import argparse
import random
import signal
import time


# Class to simulate follower growth on a social network
class FollowerSimulator:
    def __init__(self, initial_followers: int, random_range_start: int, random_range_end: int) -> None:
        self.current_followers = initial_followers  # Current number of followers
        self.total_new_followers = 0  # Total new followers gained during simulation
        self.cycles = 0  # Number of simulation cycles
        self.random_range_start = random_range_start  # Start of random range for follower growth
        self.random_range_end = random_range_end  # End of random range for follower growth

    # Simulate a single cycle of follower growth
    def simulate_cycle(self) -> None:
        new_followers = random.randint(self.random_range_start, self.random_range_end)
        new_followers += self.random_event_effect()
        self.current_followers += new_followers
        self.total_new_followers += new_followers
        self.cycles += 1
        print(f"New followers: {new_followers}, Total followers: {self.current_followers}")

    # Random events with impact over the follower count
    def random_event_effect(self) -> int:
        event: int = random.randint(1, 100)

        events = {
            (1, 5): ("You post a viral post! 🚀", (200, 300)),
            (6, 10): ("Uh-oh! A controversial post. 😬", (-60, -40)),
            (11, 15): ("It's a holiday! Extra followers! 🎄🎊", (20, 40)),
            (16, 18): ("You got mentioned by a celebrity! 🌟", (100, 200)),
            (19, 20): ("You took a social media break. 😴", (-20, -10)),
        }

        for event_range, (message, follower_range) in events.items():
            if event in range(*event_range):
                print(message)
                return random.randint(*follower_range)

        # No event for 80% of cases (event > 20)
        return 0

    # Print a summary of the simulation
    def summary(self) -> None:
        print("\n--- Simulation Summary ---")
        print(f"Simulation cycles: {self.cycles}")
        print(f"Initial followers: {self.current_followers - self.total_new_followers}")
        print(f"Total new followers: {self.total_new_followers}")
        print(f"Final number of followers: {self.current_followers}\n")

# Signal handler for clean termination
def signal_handler(signum: int, frame: None) -> None:
    raise SystemExit("Simulation terminated by user.")

# Main function
def main() -> None:
    # Initialize command-line argument parser
    parser = argparse.ArgumentParser(description="Simulate social network follower growth.")
    parser.add_argument("initial_followers", type=int,
                        help="Initial number of followers")
    parser.add_argument("random_range_start", type=int,
                        help="Starting value of random follower growth")
    parser.add_argument("random_range_end", type=int,
                        help="Ending value of random follower growth")
    parser.add_argument("-c", "--cycles", type=int, default=None,
                        help="Number of cycles to run before exiting (optional)")
    
    # Parse the arguments
    args = parser.parse_args()

    # Validate the random range
    if args.random_range_start > args.random_range_end:
        print("Error: The starting value of the random range must be less than or equal to the ending value.")
        exit(1)

    # Create simulator object
    simulator = FollowerSimulator(args.initial_followers, args.random_range_start, args.random_range_end)
    print(f"Starting with {args.initial_followers} followers.")

    # Register signal handler for clean termination
    signal.signal(signal.SIGINT, signal_handler)

    # Run simulation cycles
    try:
        while args.cycles is None or simulator.cycles < args.cycles:
            simulator.simulate_cycle()
            time.sleep(1)
    except SystemExit:
        pass
    finally:
        simulator.summary()


if __name__ == "__main__":
    main()
