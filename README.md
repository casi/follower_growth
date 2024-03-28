# follower_growth

Simulates the growth of followers for an arbitrary social network.
The program uses command-line arguments to accept the initial number of followers and a range for generating random values to simulate follower growth.

## Run

To run the program from command line:

```bash
python simulate_follower_growth.py [-h] [-c cycles] initial_followers random_range_start random_range_end
```

## Example with output

```bash
$ python simulate_follower_growth.py -c 25 100 0 10
Starting with 100 followers.
It's a holiday! Extra followers! 🎄🎊 -> 31
You post a viral post! 🚀 -> 220
You got mentioned by a celebrity! 🌟 -> 146
You took a social media break. 😴 -> -17
New: 5, By events: 380, Total: 626

-------- Simulation Summary --------
Simulation cycles........: 25
Initial followers........: 100
Total new followers......: 526
Total event followers....: 380
Percentage by events.....: 72.24%
Final number of followers: 626
```

## Tests

To run the tests from command line:

```bash
python -m unittest test_simulate_follower_growth.py
```
