"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from functools import cache

def parse_data(input_data):
    # each row is a list with 1 str and 1 tuple of ints
    # ['.??..??...?##.', (1, 1, 3)],
    values = [[s, tuple(map(int, i.split(',')))] for s, i in [v.split() for v in input_data.split('\n')]]
    return values

@cache
def count_springs(lava, springs):
    # no need to handle any leading '.'
    lava = lava.lstrip('.')
    if lava == '':
        return int(springs == ())
    if springs == ():
        return int(lava.find('#') == -1)

    # if lava starts with '#', remove the first spring
    if lava[0] == '#':
        if len(lava) < springs[0] or '.' in lava[:springs[0]]:
            return 0
        elif len(lava) == springs[0]:
            return int(len(springs) == 1)  # single spring, right size
        elif lava[springs[0]] == '#':
            return 0  # springs should be separated by '.' or '?'
        else:
            # recursive, remove one char from lava and one spring
            return count_springs(lava[springs[0] + 1:], springs[1:])

    # since we ignored leading '.' and already handles '#'
    # we now should have '?', right '?'
    # replace '?' with '#'
    return count_springs('#' + lava[1:], springs) + count_springs(lava[1:], springs)

def part1(input_data):
    # operational (.) or damaged (#)
    # groups are always separated by at least one operational spring: #### would always be 4, never 2,2).
    res = 0
    for lava, springs in input_data:
        res += count_springs(lava, springs)

    return res

def part2(input_data):
    # add '?' for each lava-stream 5 times
    # add springs 5 times
    res = 0
    for i, (lava, springs) in enumerate(input_data):
        res += count_springs('?'.join([lava] * 5), springs * 5)
    return res

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        #input_data = parse_data(puzzle.examples[0].input_data)
        input_data = [
            ['???.###', (1, 1, 3)],
            ['.??..??...?##.', (1, 1, 3)],
            ['?#?#?#?#?#?#?#?', (1, 3, 1, 6)],
            ['????.#...#...', (4, 1, 1)],
            ['????.######..#####.', (1, 6, 5)],
            ['?###????????', (3, 2, 1)],
        ]
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 2: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=12, use_example_data=False)
