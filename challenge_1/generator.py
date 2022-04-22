import random

def get_score() -> str:
    return str(random.randint(0, 100))

names = []
with open("names.txt", 'r') as f:
    for line in f:
        name = line.strip()
        names.append(name)

with open("input.txt", 'w') as f:
    for i in range(0, 100):
        f.write(f"{names[i]} {get_score()}\n")

# Goal is to calculate:
# 1. Class average
# 2. Highest Mark
# 3. Lowest Mark
# 4. Percentage student failed
