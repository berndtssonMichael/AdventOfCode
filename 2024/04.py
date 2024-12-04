

"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List


directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Up-Left
    (-1, 1),  # Up-Right
    (1, -1),  # Down-Left
    (1, 1)    # Down-Right
]

class Grid:
    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.no_of_rows = len(self.grid)
        self.no_of_cols = len(self.grid[0])

    def get(self, row_no: int, col_no: int) -> str:
        return self.grid[row_no][col_no]

    def inside_grid(self, row_no: int, col_no: int) -> bool:
        return 0 <= row_no < self.no_of_rows and 0 <= col_no < self.no_of_cols

    def word_in_grid(self, word: str, row_no: int, col_no: int, dir_row: int, dir_col: int):
        """ Check if the word exists in the grid from given position and direction"""
        for i in range(len(word)):
            r, c = row_no + i * dir_row, col_no + i * dir_col
            if not self.inside_grid(r, c) or self.get(r, c) != word[i]:
                return False
        return True

    def print_grid(self):
        for r in self.grid:
            print(''.join(r))

def parse_data(input_data) -> Grid:
    grid = Grid([list(v) for v in input_data.split('\n')])
    return grid

def part1(grid: Grid) -> int:

    word = 'XMAS'
    result = 0
    for row in range(grid.no_of_rows):
        for col in range(grid.no_of_cols):
            # check first pos
            if grid.get(row, col) == word[0]:
                for dir_row, dir_col in directions:
                    if grid.word_in_grid(word, row, col, dir_row, dir_col):
                        result += 1
    return result


def part2(grid: Grid) -> int:
    """ A different approach, create a list of what we are looking for, word and word reversed
    Skip the outer rows and cols, since we are searching for a 3 letter word
    """
    word = 'MAS'
    words = [word, word[::-1]]
    find_char = word[1]  # the middel char
    result = 0

    # We are looking for words 3 chars long, so we can skip some parts of the grid
    for row in range(1, grid.no_of_rows - 1):  # skip first and last row
        for col in range(1, grid.no_of_cols - 1):

            # check if current posision is middle letter
            if grid.get(row, col) == find_char:
                left_to_right = grid.get(row - 1, col - 1) + grid.get(row, col) + grid.get(row + 1, col + 1)
                right_to_left = grid.get(row - 1, col + 1) + grid.get(row, col) + grid.get(row + 1, col - 1)
                if left_to_right in words and right_to_left in words:
                    result += 1
    return result

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = puzzle.examples[0].input_data
    else:
        input_data = puzzle.input_data

    # create grid
    grid = parse_data(input_data)

    print(f'Part 1: {part1(grid)}')
    print(f'Part 2: {part2(grid)}')


if __name__ == '__main__':

    solve_puzzle(year=2024, day=4, use_example_data=False)
