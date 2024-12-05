

"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple, NamedTuple

class Rule(NamedTuple):
    before: int
    after: int


def parse_data(input_data: str) -> Tuple[List[Rule], List[List[int]]]:
    """ Split input into rules and updates"""
    rules_data, updates_data = input_data.strip().split('\n\n')
    updates = [list(map(int, line.split(','))) for line in updates_data.splitlines()]
    rules = [Rule(*map(int, line.split('|'))) for line in rules_data.splitlines()]
    return rules, updates

def is_update_valid(update: List[int], rules: List[Rule]) -> bool:
    for rule in rules:
        if rule.before in update and rule.after in update:
            if update.index(rule.before) > update.index(rule.after):
                return False
    return True

def reorder_update(update: List[int], rules: List[Rule]) -> List[int]:
    # copy update list
    reorded_update = list(update)
    is_unorded = True

    while is_unorded:
        is_unorded = False
        for rule in rules:
            if rule.before in reorded_update and rule.after in reorded_update:
                before_idx = reorded_update.index(rule.before)
                after_idx = reorded_update.index(rule.after)
                # Swap places if needed
                if before_idx > after_idx:
                    reorded_update.pop(after_idx)
                    reorded_update.insert(before_idx + 1, rule.after)
                    is_unorded = True

    return reorded_update


def part1(rules: List[Rule], updates: List[List[int]]) -> int:

    result = 0
    for update in updates:
        if is_update_valid(update, rules):
            result += update[len(update) // 2]
    return result

def part2(rules: List[Rule], updates: List[List[int]]) -> int:

    result = 0
    for update in updates:
        if not is_update_valid(update, rules):
            update = reorder_update(update, rules)
            result += update[len(update) // 2]
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
