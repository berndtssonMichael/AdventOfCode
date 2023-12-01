"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List

def parse_data(input_data) -> List[str]:
    values = [v for v in input_data.split('\n')]
    return values

def do_stuff(input_data):

    return input_data

def part1(input_data) -> int:

    return input_data

def part2(input_data) -> int:

    return input_data

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2022, day=1, use_example_data=False)
