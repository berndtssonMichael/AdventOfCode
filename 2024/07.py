

"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List, Tuple
from itertools import product
from time import perf_counter


def parse_data(input_data: str) -> List[Tuple[int, List[int]]]:
    """ Split data to rows with result (int) and equation (list of ints)"""
    data = []
    for line in input_data.splitlines():
        v, s = line.split(':')
        data.append((int(v), list(map(int, s.strip().split()))))
    return data


def find_valid_results(data: List[Tuple[int, List[int]]], operators) -> int:

    result = 0
    for answer, equation in data:

        no_operators = len(equation) - 1

        for comb in product(operators, repeat=no_operators):
            # fetch first digit
            res = equation[0]
            for i in range(len(comb)):
                if comb[i] == '||':
                    res = int(f'{res}{equation[i + 1]}')
                elif comb[i] == '+':
                    res += equation[i + 1]
                else:
                    res *= equation[i + 1]
                if res > answer:
                    break
            if res == answer:
                result += res
                break

    return result


def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        input_data = parse_data(puzzle.input_data)

    # t1_start = perf_counter()
    print(f"Part 1: {find_valid_results(input_data, operators=['+', '*'])}")
    # t2_start = perf_counter()
    print(f"Part 2: {find_valid_results(input_data, operators=['+', '*', '||'])}")
    # t1_end = perf_counter()
    # print(f'execution part1: {t2_start - t1_start}, part2: {t1_end - t2_start}, total: {t1_end - t1_start}')

if __name__ == '__main__':

    solve_puzzle(year=2024, day=7, use_example_data=False)
