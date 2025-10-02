# this is an implementation of my algorithm for simulating a simple evolutionary system
# Check-Darwin Algorithm
# It first generates a random float number between 0 and 1, if the number is higher than the mutation rate, it mutates one of the traits of the creature by adding or subtracting 1 from it (with a minimum of 1 and a maximum of 10).
# If the number is lower than the mutation rate, it creates an offspring with the same traits as the parent.

import random


def check_darwin_algorithm(mutation_rate:float):
    return random.uniform(0, 1) > mutation_rate


print(check_darwin_algorithm(0))
