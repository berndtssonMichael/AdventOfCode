"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Set, NamedTuple

# Handle directions as N, S, E, W

class Coord(NamedTuple):
    row: int
    col: int

class Beam(NamedTuple):
    position: Coord
    direction: str


class Grid:
    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.no_of_rows = len(self.grid)
        self.no_of_cols = len(self.grid[0])

    def get(self, coord: Coord) -> str:
        return self.grid[coord.row][coord.col]

    def inside_grid(self, coord: Coord) -> bool:
        #return coord.row < 0 or coord.row >= len(grid) or coord.col < 0 or coord.col >= len(grid[0])
        return 0 <= coord.row < self.no_of_rows and 0 <= coord.col < self.no_of_cols

    def print_grid(self):
        for r in self.grid:
            print(''.join(r))

def parse_data(input_data) -> Grid:
    grid = Grid([list(v) for v in input_data.split('\n')])
    return grid


def follow_beam(beam: Beam, visited: Set[Beam], grid: Grid) -> Set[Beam]:
    if beam not in visited:
        visited.add(beam)

    while True:
        (row, col), direction = beam
        #match grid.grid[row][col]:
        match grid.get(beam.position):
            case '.':
                pass
            case '/':
                match direction:
                    case 'N':
                        direction = 'E'
                    case 'S':
                        direction = 'W'
                    case 'E':
                        direction = 'N'
                    case 'W':
                        direction = 'S'
            case '\\':
                match direction:
                    case 'N':
                        direction = 'W'
                    case 'S':
                        direction = 'E'
                    case 'E':
                        direction = 'S'
                    case 'W':
                        direction = 'N'
            case '/':
                match direction:
                    case 'N':
                        direction = 'E'
                    case 'S':
                        direction = 'W'
                    case 'E':
                        direction = 'N'
                    case 'W':
                        direction = 'S'
            case '-':
                match direction:
                    case 'N':
                        direction = 'E'
                        # split 'W'
                        visited = follow_beam(Beam(beam.position, 'W'), visited, grid)
                    case 'S':
                        direction = 'W'
                        # split 'E
                        visited = follow_beam(Beam(beam.position, 'E'), visited, grid)
                    case 'E':
                        pass
                    case 'W':
                        pass
            case '|':
                match direction:
                    case 'N':
                        pass
                    case 'S':
                        pass
                    case 'E':
                        direction = 'N'
                        # split 'S'
                        visited = follow_beam(Beam(beam.position, 'S'), visited, grid)
                    case 'W':
                        direction = 'S'
                        # 'split 'N'
                        visited = follow_beam(Beam(beam.position, 'N'), visited, grid)

        # update position depending on new direction
        match direction:
            case 'N':
                row -= 1
            case 'S':
                row += 1
            case 'E':
                col += 1
            case 'W':
                col -= 1

        beam = Beam(Coord(row, col), direction)
        # visited or out of bounds
        if beam in visited or not grid.inside_grid(beam.position):
            break
        else:
            visited.add(beam)

    return visited

def part1(grid: Grid) -> int:
    start = Beam(Coord(0, 0), 'E')
    visited = follow_beam(start, set(), grid)

    return len(set(val[0] for val in visited))

def part2(grid: Grid) -> int:
    tiles = 0

    # test first and last column
    for r in range(grid.no_of_rows):
        for pos in ((0, 'E'), (grid.no_of_cols - 1, 'W')):
            res = len(set(val[0] for val in follow_beam(Beam(Coord(r, pos[0]), pos[1]), set(), grid)))
            tiles = max(tiles, res)

    # test first and last row
    for c in range(grid.no_of_cols):
        for pos in ((0, 'S'), (grid.no_of_rows - 1, 'N')):
            res = len(set(val[0] for val in follow_beam(Beam(Coord(pos[0], c), pos[1]), set(), grid)))
            tiles = max(tiles, res)
    return tiles

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
        #for row in input_data:
        #    print(''.join(row))
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=16, use_example_data=False)
