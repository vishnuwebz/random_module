# 2 dice rolling game

import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

print(f"Dice Rolls: {roll_dice(2)}")

# Dice Rolls: [6, 6]
