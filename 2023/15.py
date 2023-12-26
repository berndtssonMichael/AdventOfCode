"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List


def parse_data(input_data) -> List[str]:
    values = [v for v in input_data.split(',')]
    return values

def hash(string):
    i = 0
    for c in string:
        i += ord(c)
        i *= 17
        i %= 256
    return i


def part1(input_data) -> int:

    return sum(hash(data) for data in input_data)

def part2(input_data) -> int:

    # create empty boxes
    boxes = [[] for _ in range(256)]
    # dict with focal length
    focals = {}

    for data in input_data:
        if '=' in data:
            label, focal = data.split('=')
            focal = int(focal)
            b = hash(label)
            focals[label] = focal

            if label in boxes[b]:
                i = boxes[b].index(label)
                boxes[b][i] = label
            else:
                boxes[b].append(label)

        elif data.endswith('-'):
            label = data[:-1]
            b = hash(label)
            if label in boxes[b]:
                boxes[b].remove(label)

    res = 0
    for box_ix, box in enumerate(boxes, start=1):
        for slot_ix, label in enumerate(box, start=1):
            res += box_ix * slot_ix * focals[label]
    return res

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

    solve_puzzle(year=2023, day=15, use_example_data=False)
