"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple

def parse_data(input_data) -> List[Tuple[int, str]]:
    # return list with typles like: (1, '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    values = []
    for line in input_data.split('\n'):
        game, cubes = line.split(': ')
        # convert game to int
        game = int(game.split(' ')[1])
        cube_sets = [cube.strip() for cube in cubes.split(';')]
        colors = [
            {cube.split(' ')[1]: int(cube.strip().split(' ')[0]) for cube in cubes.split(', ')}
            for cubes in cube_sets
        ]
        values.append((game, colors))
    return values

def do_stuff(input_data):

    return input_data

def part1(input_data) -> int:
    res = 0
    for id, games in input_data:
        for game in games:
            if not (game.get('red', 0) <= 12
                    and game.get('green', 0) <= 13
                    and game.get('blue', 0) <= 14):
                break
        else:
            res += id

    return res

def part2(input_data) -> int:
    res = 0
    for _, games in input_data:
        red, green, blue = (0, 0, 0)
        for game in games:
            red = max(red, game.get('red', 0))
            green = max(green, game.get('green', 0))
            blue = max(blue, game.get('blue', 0))
        res += red * green * blue

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

    solve_puzzle(year=2023, day=2, use_example_data=False)
