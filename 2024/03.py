"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
import re

def part1(input_data: str) -> int:
    """ Use regex to parse out intstructions mul(<1-3 digits>, <1-3 digits>)
    """

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_data)
    result = [int(v1) * int(v2) for v1, v2 in matches]

    return sum(result)

def part2(input_data: str) -> int:
    """ Use regex to split instructions to groups with mul, don't() and do()
        Reuse part1 to calc each mul instruction
    """
    result = 0
    do_calc = True
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)"
    matches = list(re.findall(pattern, input_data))

    for m in matches:
        if m.startswith('mul') and do_calc:
            result += part1(m)
        elif m == "don't()":
            do_calc = False
        elif m == "do()":
            do_calc = True
    return result

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = puzzle.examples[0].input_data
    else:
        input_data = puzzle.input_data

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2024, day=3, use_example_data=False)
