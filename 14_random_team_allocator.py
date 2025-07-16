# 3 : Random Team Allocator

import random

def allocate_teams(players, team_size):
    random.shuffle(players)
    return [players[i:i + team_size] for i in range(0, len(players), team_size)]

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

print(f"Teams: {allocate_teams(players, 2)}")