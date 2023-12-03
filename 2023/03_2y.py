"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle  # type: ignore
from typing import List, Tuple, DefaultDict
from collections import defaultdict
from itertools import takewhile

def parse_data(input_data: str) -> List[List[str]]:
    # return grid data
    values: List[List[str]] = [list(v) for v in input_data.split('\n')]
    return values

def solve_both(grid: List[List[str]]) -> Tuple[int, int]:
    ROWS = len(grid)
    COLS = len(grid[0])

    numbers: List[int] = []
    possible_gears: DefaultDict[Tuple[int], List[int]] = defaultdict(list)

    def has_symbol(r: int, c: int, num: str) -> bool:
        """
        r, current row
        c, end possition of number
        num, number to check
        """
        num_length = len(num)
        # neighbour rows
        for nr in [-1, 0, 1]:
            # neighbour cols
            for nc in [-1, 0, 1]:
                for i in range(num_length):
                    row_pos, col_pos = r + nr, c + nc + i
                    if 0 <= row_pos < ROWS and 0 <= col_pos < COLS:
                        char = grid[row_pos][col_pos]
                        if not char.isdigit() and char != '.':
                            # part 2
                            if char == '*':
                                possible_gears[(row_pos, col_pos)].append(int(num))
                            return True
        return False

    for r in range(ROWS):
        c = 0
        while c < (COLS - 1):
            if grid[r][c].isdigit():
                # find full number
                num_str = ''.join(takewhile(lambda c: c.isdigit(), grid[r][c:]))
                if has_symbol(r, c, num_str):
                    numbers.append(int(num_str))
                c += len(num_str)
                num_str = ''
            else:
                c += 1

    gears = [v[0] * v[1] for v in possible_gears.values() if len(v) == 2]
    return (sum(numbers), sum(gears))


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data: str = parse_data(puzzle.examples[0].input_data)  # type: ignore
    else:
        input_data: str = parse_data(puzzle.input_data)  # type: ignore

    part1, part2 = solve_both(input_data)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=3, use_example_data=False)
