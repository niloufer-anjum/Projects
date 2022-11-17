""" On average, how many flips are needed for a sequence to contain
both heads and tails. A simulation that runs 10,000 trials of the experiment and
prints the average number of flips per trial. """

import random


# 0 - heads, 1 - tails
def flip_count():
    flips_count = 0
    side = None
    while True:
        flip = random.randint(0,1)
        flips_count += 1
        if side == flip:
            break
        else:
            side = flip
    
    return flips_count


def trail_count(trials):
    flips_avg = []
    for i in range(trials):
        flips_avg.append(flip_count())
    
    return sum(flips_avg)/trials


print(trail_count(10_000))





