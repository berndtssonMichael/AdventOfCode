from itertools import product
from collections import Counter
from functools import lru_cache
from typing import Tuple

class Player():
    def __init__(self, id: str, start_pos: int):
        self.id = id
        self.pos = start_pos - 1  # make position zero-based
        self.score = 0

    def __str__(self) -> str:
        return f'Player: {self.id}, current pos: {self.pos}, score: {self.score}'

    def calc_score(self, steps):
        _pos = (self.pos + steps) % 10
        self.score += _pos + 1  # add one to score since position now i zero-based
        self.pos = _pos

class Dice():
    def __init__(self):
        self.number = 0  # init at zero
        self.total_count = 0

    def __str__(self):
        return f'Dice current number {self.number}, total count: {self.total_count}'

    def throw_dice(self, throws):
        for _ in range(1, throws + 1):
            self.number += 1
            self.total_count += 1
            if self.number == 101:
                self.number = 1
        steps = (self.number * throws) - throws
        return steps


class DiracDice():
    # 3 sides
    def __init__(self):
        self.number = 0  # init at zero
        self.total_count = 0
        self.total_universe = 0

    def __str__(self):
        return f'Dice current number {self.number}, total count: {self.total_count}'

    def throw_dice(self, throws):
        for _ in range(1, throws + 1):
            self.number += 1
            self.total_count += 1
            if self.number == 101:
                self.number = 1
        steps = (self.number * throws) - throws

        return steps

def play_a(p1, p2):
    dice = Dice()
    loser = None
    max_score = 1000
    # solve A
    while True:
        p1.calc_score(dice.throw_dice(3))
        if p1.score >= max_score:
            loser = p2
            break
        p2.calc_score(dice.throw_dice(3))
        if p2.score >= max_score:
            loser = p1
            break
        # print(p1, p2.score)
    # print(f'Answer A: {p2.score * dice.total_count}')
    return loser.score * dice.total_count


@lru_cache(maxsize=None)    # <-- Cache the results of the function
                            # (when the function is called with the same parameters, it returns the same result without being executed)
def dirac_dice(p1_pos: int, p2_pos: int, p1_score: int = 0, p2_score: int = 0) -> Tuple[int, int]:
    global dice_sums

    # Return the win count when a player reaches 21 points
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)

    # Cumulative amount of wins for each player
    p1_wins_total = 0
    p2_wins_total = 0

    # Iterate over all possible rolls in a turn
    for roll, amount in dice_sums.items():

        # Move the player and increment their score
        p1_pos_new = (p1_pos + roll) % 10
        p1_score_new = p1_score + p1_pos_new + 1

        # Pass the turn to the other player
        p2_wins, p1_wins = dirac_dice(p2_pos, p1_pos_new, p2_score, p1_score_new)

        # Increment the win counter by the results multiplied by the amount of times the roll repeats
        p1_wins_total += p1_wins * amount
        p2_wins_total += p2_wins * amount

    # Returns the final tally of victories
    return (p1_wins_total, p2_wins_total)


# test-data
# p1 = Player('p1', 4)
# p2 = Player('p2', 8)

# real input
p1 = Player('p1', 10)
p2 = Player('p2', 9)

print(f'Answer A: {play_a(p1, p2)}')

# real input
p1b = Player('p1b', 10)
p2b = Player('p2b', 9)

dice_sums = Counter(sum(rolls) for rolls in product((1, 2, 3), repeat=3))

# solve b
max_victories = max(
    dirac_dice(
        p1_pos = p1b.pos,
        p2_pos = p2b.pos
    )
)

print(max_victories)
