"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple
from dataclasses import dataclass, field
from collections import deque
import sys

sys.setrecursionlimit(10000)
"""
Created a dataclass just for practice, after all it is sunday :)
"""
@dataclass
class Grid:
    rows: List[List[str]] = field(default_factory=list)

    @staticmethod
    def from_string(input_data: str) -> 'Grid':
        grid_rows = [list(v) for v in input_data.split('\n')]
        return Grid(grid_rows)

    @property
    def no_of_rows(self) -> int:
        return len(self.rows)

    @property
    def no_of_cols(self) -> int:
        return len(self.rows[0])

    def char(self, pos: Tuple[int, int]) -> str:
        return self.rows[pos[0]][pos[1]]

    def get_start_pos(self, start_char) -> Tuple[int, int]:
        for r, row in enumerate(self.rows):
            if 'S' in row:
                pos = (r, row.index(start_char))
                return pos
        raise ValueError(f"Did not find '{start_char}' in grid")

    def print_grid(self, visited: List[Tuple[int, int]]):
        marker = 'X'
        empty = ' '
        print('_' * self.no_of_cols)
        for r in range(self.no_of_rows):
            row = ''
            for c in range(self.no_of_cols):
                row += marker if (r, c) in visited else empty

            print(row)
        # last row
        print('_' * self.no_of_cols)

# describe change in direction, and the opposite direction
directions = {
    'N': (-1, 0, 'S'),
    'S': (1, 0, 'N'),
    'E': (0, 1, 'W'),
    'W': (0, -1, 'E'),
}

# how are the pipes join
pipe_joins = {
    '|': {'N', 'S'},
    '-': {'E', 'W'},
    'L': {'N', 'E'},
    'J': {'N', 'W'},
    '7': {'S', 'W'},
    'F': {'S', 'E'},
    # starting point is possibly connected to all directions
    'S': {'N', 'S', 'E', 'W'},
}

# function for Breadth-First Search
def bfs(grid: Grid, start: Tuple[int, int], return_visited: bool = False, print_grid: bool = False) -> int:
    no_of_rows = grid.no_of_rows
    no_of_cols = grid.no_of_cols

    visited = dict()
    # the queue describes position and distance
    queue = deque([(start, 0)])

    while queue:
        curr_pos, dist = queue.popleft()  # pos = (r, c)
        if curr_pos in visited:
            continue
        visited[curr_pos] = dist

        for direction in pipe_joins[grid.char(curr_pos)]:

            dx, dy, opposite_direction = directions[direction]
            next_pos = (curr_pos[0] + dx, curr_pos[1] + dy)

            if 0 <= next_pos[0] < no_of_rows and 0 <= next_pos[1] < no_of_cols and grid.char(next_pos) in pipe_joins:

                target = pipe_joins[grid.char(next_pos)]
                if opposite_direction in target:
                    queue.append((next_pos, dist + 1))

    if print_grid:
        grid.print_grid(visited.keys())
    if return_visited:
        return list(visited.keys())
    return max(visited.values())

def part1(grid: Grid) -> int:
    return bfs(grid, grid.get_start_pos('S'), return_visited=False, print_grid=False)

def part2(grid: Grid) -> int:
    # get all visited coords
    visited = bfs(grid, grid.get_start_pos('S'), return_visited=True, print_grid=False)

    for r in range(grid.no_of_rows):
        norths = 0
        for c in range(grid.no_of_cols):
            if (r, c) in visited:
                # can we go north from this col
                if 'N' in pipe_joins[grid.char((r, c))]:
                    norths += 1
                continue
            # if no of norths is odd, we are inside
            if norths % 2 != 0:
                grid.rows[r][c] = 'I'

    return sum(row.count('I') for row in grid.rows)


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        raw = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
        grid = Grid.from_string(raw)
    else:
        grid = Grid.from_string(puzzle.input_data)
    print(f'Part 1: {part1(grid)}')
    print(f'Part 2: {part2(grid)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=10, use_example_data=False)
