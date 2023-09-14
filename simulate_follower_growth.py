import argparse
import random
import signal
import time


def signal_handler(signum, frame):
    """
    Handle signal for clean termination.

    Parameters:
    - signum: Signal number
    - frame: Current stack frame

    Returns:
    None
    """
    raise SystemExit("Simulation terminated by user.")


def simulate_follower_growth(initial_followers, random_range_start, random_range_end):
    """
    Simulate the growth of followers over time.

    Parameters:
    - initial_followers: The initial number of followers
    - random_range_start: The starting value of the random range for simulating follower growth
    - random_range_end: The ending value of the random range for simulating follower growth

    Returns:
    None
    """
    current_followers = initial_followers
    total_new_followers = 0
    cycles = 0

    print(f"Starting with {initial_followers} followers.")

    try:
        while True:
            # Generate a random number of new followers within the specified range
            new_followers = random.randint(
                random_range_start, random_range_end)

            # Update the current number of followers
            current_followers += new_followers
            total_new_followers += new_followers
            cycles += 1

            print(
                f"New followers: {new_followers}, Total followers: {current_followers}")

            # Pause for 5 seconds before simulating the next cycle
            time.sleep(5)
    except SystemExit:
        print("\n--- Simulation Summary ---")
        print(f"Initial followers: {initial_followers}")
        print(f"Total new followers gained: {total_new_followers}")
        print(f"Final number of followers: {current_followers}")
        print(f"Simulation cycles completed: {cycles}")


if __name__ == "__main__":
    # Initialize command-line argument parser
    parser = argparse.ArgumentParser(
        description="Simulate social network follower growth.")

    # Add arguments for initial followers and random range
    parser.add_argument("initial_followers", type=int,
                        help="Initial number of followers")
    parser.add_argument("random_range_start", type=int,
                        help="Starting value of random follower growth")
    parser.add_argument("random_range_end", type=int,
                        help="Ending value of random follower growth")

    # Parse the arguments
    args = parser.parse_args()

    # Validate that random_range_start is less than or equal to random_range_end
    if args.random_range_start > args.random_range_end:
        print("Error: The starting value of the random range must be less than or equal to the ending value.")
        exit(1)

    # Register signal handler for clean termination
    signal.signal(signal.SIGINT, signal_handler)

    # Run the simulation with the parsed arguments
    simulate_follower_growth(args.initial_followers,
                             args.random_range_start, args.random_range_end)
