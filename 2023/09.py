"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List

def parse_data(input_data) -> List[List[int]]:
    print(input_data)
    values = [[int(i) for i in v.split()] for v in input_data.split('\n')]

    return values

def parse_file() -> List[List[int]]:
    # for some reason fetching day 9 did not work so donwloaded file manually!
    lines = [[int(i) for i in line.split()] for line in open("input/input09.txt").read().splitlines()]
    return lines

def extrapolate(data) -> int:

    if all(i == 0 for i in data):
        return 0
    numbers = []
    for i in range(len(data) - 1):
        numbers.append(data[i + 1] - data[i])

    return data[-1] + extrapolate(numbers)

def part1(input_data) -> int:
    return sum((extrapolate(data) for data in input_data))

def part2(input_data) -> int:
    # just reverse each line
    return sum((extrapolate(data[::-1]) for data in input_data))

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        #input_data = parse_data(puzzle.input_data)
        input_data = parse_file()

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=9, use_example_data=False)
