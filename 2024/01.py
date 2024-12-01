"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple

def parse_data(input_data) -> Tuple[List[int], List[int]]:
    """ Return left and right data as sorted lists"""

    # left = []
    # right = []
    # for line in input_data.split('\n'):
    #     values = line.split()
    #     left.append(int(values[0]))
    #     right.append(int(values[1]))

    # Just for practice, I tried a oneliner
    left, right = zip(*((int(values[0]), int(values[1]))
                        for values in (line.split()
                                       for line in input_data.split('\n'))))

    return sorted(left), sorted(right)

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = puzzle.examples[0].input_data
    else:
        input_data = puzzle.input_data

    left_list, right_list = parse_data(input_data)

    print(f'Part 1: {sum([abs(left - right) for left, right in (zip(left_list, right_list))])}')
    print(f'Part 2: {sum([num * right_list.count(num) for num in left_list])}')

if __name__ == '__main__':

    solve_puzzle(year=2024, day=1, use_example_data=False)
