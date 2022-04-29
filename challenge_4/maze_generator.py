# Phoebe you should read this code too to see if this makes sense to you.
# It won't help you with this challenge, but just for general knowledge
# The purpose of this is to generate a maze of size 20 x 50.
# There may not be a path. I manually edited the output to create a path.

import random
random.uniform(0, 1)

width = 50
height=20

for h in range(height):
    for w in range(width):
        coin_flip = random.uniform(0, 1)
        if coin_flip < 0.5:
            print("*", end='')
        else:
            print(" ", end='')
    # force a new line
    print("")
