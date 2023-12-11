"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle


def parse_data(input_data):
    values = [[c for c in line] for line in input_data.split('\n')]
    return values

def calc_shortest_path(input_data, universe_expansion: int) -> int:

    res = 0
    rows = len(input_data)
    cols = len(input_data[0])
    assert rows == cols, 'Uneaven number of cols and rows'

    empty_rows = []
    empty_cols = []

    # assuming equal numbers or rows and columns
    # find empty rows and cols
    for i in range(rows):
        if '#' not in input_data[i]:
            empty_rows.append(i)
        if '#' not in [input_data[j][i] for j in range(cols)]:
            empty_cols.append(i)

    # where are the stars
    galaxies = []
    for r in range(rows):
        for c in range(cols):
            if input_data[r][c] == '#':
                galaxies.append((r, c))

    # start on first galaxy
    for ix, (row1, col1) in enumerate(galaxies):
        # iterate over the remaining to calc dist
        for g2 in range(ix, len(galaxies)):

            row2, col2 = galaxies[g2]
            dist = abs(row2 - row1) + abs(col2 - col1)
            # add for universe expansion
            for empty_row in empty_rows:
                if min(row2, row1) <= empty_row <= max(row2, row1):
                    dist += universe_expansion
            for empty_col in empty_cols:
                if min(col2, col1) <= empty_col <= max(col2, col1):
                    dist += universe_expansion
            res += dist
    return res

def part1(input_data) -> int:
    # expansion "twice as big" -> 2 then remove 1
    expansion = 2 - 1
    return calc_shortest_path(input_data, expansion)

def part2(input_data) -> int:
    # expansion "one million times" -> 1 000 000 then remove 1
    expansion = 1000000 - 1
    return calc_shortest_path(input_data, expansion)

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

    solve_puzzle(year=2023, day=11, use_example_data=False)
