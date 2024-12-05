

"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple
from functools import cmp_to_key


def parse_data(input_data: str) -> Tuple[List[Tuple[int, ...]], List[List[int]]]:
    """ Split input into rules and updates"""
    rules_data, updates_data = input_data.strip().split('\n\n')
    rules = [tuple(map(int, line.split('|'))) for line in rules_data.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_data.splitlines()]
    return rules, updates

def part1(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    result = 0
    for update in updates:
        if update == sorted(update, key=cmp_to_key(
                lambda a, b: 1 if (b, a) in rules else -1)):
            result += update[len(update) // 2]
    return result

def part2(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    result = 0
    for update in updates:
        if update != (new_update := sorted(update, key=cmp_to_key(
                lambda a, b: 1 if (b, a) in rules else -1))):
            result += new_update[len(new_update) // 2]
    return result


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = puzzle.examples[0].input_data
    else:
        input_data = puzzle.input_data

    rules, updates = parse_data(input_data)

    print(f'Part 1: {part1(rules, updates)}')
    print(f'Part 2: {part2(rules, updates)}')


if __name__ == '__main__':

    solve_puzzle(year=2024, day=5, use_example_data=False)
