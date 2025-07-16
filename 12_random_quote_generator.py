# 1 random quote generator

import random

quotes = [
    "Be the change you wish to see in the world.",
    "Stay hungry, stay foolish.",
    "The only way to do great work is to love what you do."
]

def get_random_quote():
    return random.choice(quotes)
print("Random Quote:", get_random_quote())

