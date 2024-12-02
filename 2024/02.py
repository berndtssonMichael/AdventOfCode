"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple

def parse_data(input_data) -> List[List[int]]:

    values = []
    for row in input_data.split('\n'):
        values.append([int(v) for v in row.split()])
    return values

def check_row_part1(row: List[int]) -> bool:
    """ Check of row values are increasing or descresing by 1 to 3 """
    is_increasing = all(1 <= row[i + 1] - row[i] <= 3 for i in range(len(row) - 1))
    is_decreasing = all(1 <= row[i] - row[i + 1] <= 3 for i in range(len(row) - 1))
    return is_increasing or is_decreasing

def check_row_part2(row: List[int]) -> bool:
    """ First check the row by first example
    If still not OK create new sublists by removing one item at a time """

    if check_row_part1(row):
        return True

    for i in range(len(row)):
        if check_row_part1(row[:i] + row[i + 1:]):
            return True
    return False


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {sum([check_row_part1(row) for row in input_data])}')
    print(f'Part 2: {sum([check_row_part2(row) for row in input_data])}')

if __name__ == '__main__':

    solve_puzzle(year=2024, day=2, use_example_data=False)
