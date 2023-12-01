"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List

def parse_data(input_data) -> List[str]:
    values = [v for v in input_data.split('\n')]
    return values

def get_values(values: List[str]) -> List[int]:
    """ filter out digits in the list of strings
        return first and last digit
    """
    digits = []
    for input in values:
        all_digits = ''.join(filter(str.isdigit, input))
        digits.append(int(all_digits[0] + all_digits[-1]))
    return digits

def convert_words_to_numbers(values: List[str]) -> List[str]:
    """ find words that are numbers and add correspondig number to the string
    """
    word_to_num = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    new_list = []
    for value in values:
        number_str = ''
        for i in range(len(value)):
            number_str += value[i]  # rebuild the string, char by char
            for word, number in word_to_num.items():
                # Check if a word starts at the current index, since word could be overlapping 'eightwo' - 82
                if value[i:].startswith(word):
                    number_str += number  # Add the corresponding number to the string
                    break

        new_list.append(number_str)
    return get_values(new_list)

def part1(input_data) -> int:
    values = get_values(input_data)
    return (sum(values))

def part2(input_data) -> int:
    values = convert_words_to_numbers(input_data)
    return (sum(values))

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        input_data = parse_data(puzzle.examples[0].input_data)
    else:
        input_data = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(input_data)}')
    print(f'Part 1: {part2(input_data)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=1, use_example_data=False)
