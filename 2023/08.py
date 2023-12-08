"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Dict, Tuple
from math import lcm

def parse_data(input_data) -> Tuple[str, Dict[str, Tuple[str, str]]]:

    values = [v for v in input_data.split('\n')]
    directions = values[0]

    node_map = {key: tuple(value.strip('()').split(', ')) for line in values[2:] for key, value in [line.split(' = ')]}
    return directions, node_map

def part1(directions: str, node_map: Dict[str, Tuple[str, str]]) -> int:

    steps: int = 0
    current_position: str = 'AAA'
    found_target: bool = False
    while not found_target:
        # loop over the available directions
        for dir in directions:
            steps += 1
            # if dir == 'R', we get True -> 1 otherwise 0
            current_position = node_map[current_position][dir == 'R']
            if current_position == 'ZZZ':
                found_target = True
                break

    return steps

def part2(directions: str, node_map: Dict[str, Tuple[str, str]]) -> int:

    positions = [k for k in node_map.keys() if k.endswith('A')]
    distance = dict()
    for current_position in positions:
        steps: int = 0
        start_pos = current_position
        found_target: bool = False
        while not found_target:
            # loop over the available directions
            for dir in directions:
                steps += 1
                # if dir == 'R', we get True -> 1 otherwise 0
                current_position = node_map[current_position][dir == 'R']
                if current_position.endswith('Z'):
                    found_target = True
                    break

        distance[start_pos] = steps
    # now we have the distance for each starting point
    # use math.lcm for calculating the result
    # OK, I had to Google this :)
    return lcm(*[v for v in distance.values()])


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        directions, node_map = parse_data(puzzle.examples[0].input_data)
    else:
        directions, node_map = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(directions, node_map)}')
    print(f'Part 2: {part2(directions, node_map)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=8, use_example_data=False)
