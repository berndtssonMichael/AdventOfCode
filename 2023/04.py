"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle  # type: ignore
from typing import List, Tuple, DefaultDict
from collections import defaultdict

def parse_data(input_data: str) -> List[Tuple[List[int], List[int]]]:
    # return list with typles of set
    values: List[Tuple[List[int], List[int]]] = []
    for line in input_data.split('\n'):
        _, cards = line.split(': ')
        set1, set2 = [card.strip() for card in cards.split(' | ')]

        winning_cards = [int(nr) for nr in set1.split()]
        current_cards = [int(nr) for nr in set2.split()]

        values.append((winning_cards, current_cards))

    return values


def solve_part_1_and_2(input_data: List[Tuple[List[int], List[int]]]) -> Tuple[int, int]:
    total_points = 0
    # part 2
    # store how many of each card I get, key: card_no, value: number of cards
    no_of_cards: DefaultDict[int, int] = defaultdict(int)
    card_no = 0
    for cards in input_data:
        card_no += 1
        # intersection of the two card-sets
        no_of_wins = len(set(cards[0]).intersection(set(cards[1])))
        if no_of_wins:
            total_points += int(2 ** (no_of_wins - 1))

        # count cards for part 2
        # add original card
        no_of_cards[card_no] += 1
        # how many extra cards ?
        for extra_card in range(card_no + 1, card_no + no_of_wins + 1):
            no_of_cards[extra_card] += no_of_cards[card_no]

    return total_points, sum(no_of_cards.values())

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)  # type: ignore
    else:
        input_data = parse_data(puzzle.input_data)  # type: ignore

    part1, part2 = solve_part_1_and_2(input_data)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=4, use_example_data=False)
