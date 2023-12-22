"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle

def parse_data(input_data):
    nested_list = [[list(row) for row in group.split('\n')] for group in input_data.split('\n\n')]
    return nested_list

def transpose_list(data):
    return list(map(list, zip(*data)))

def find_reflections(grid, smudges=0) -> int:
    # only checking rows, for column the grid needs to be transposed

    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        # check number of differeces, should be none in part 1
        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == smudges
        ):
            return r

    return 0

def part1(input_data) -> int:
    res = 0
    for grid in input_data:
        # horisontal
        res += find_reflections(grid) * 100
        # vertical
        res += find_reflections(transpose_list(grid))

    return res


def part2(input_data) -> int:
    res = 0
    smudges = 1
    for grid in input_data:
        # horisontal
        res += find_reflections(grid, smudges) * 100
        # vertical
        res += find_reflections(transpose_list(grid), smudges)

    return res


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
        # input_data = [[
        #     '#...##..#',
        #     '#....#..#',
        #     '..##..###',
        #     '#####.##.',
        #     '#####.##.',
        #     '..##..###',
        #     '#....#..#',
        # ]]
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=13, use_example_data=False)
