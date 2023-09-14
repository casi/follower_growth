import argparse
import random
import time


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

    print(f"Starting with {initial_followers} followers.")

    while True:
        # Generate a random number of new followers within the specified range
        new_followers = random.randint(random_range_start, random_range_end)

        # Update the current number of followers
        current_followers += new_followers

        print(
            f"New followers: {new_followers}, Total followers: {current_followers}")

        # Pause for 2 seconds before simulating the next cycle
        time.sleep(2)


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

    # Run the simulation with the parsed arguments
    simulate_follower_growth(args.initial_followers,
                             args.random_range_start, args.random_range_end)

