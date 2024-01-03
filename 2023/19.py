"""
    Using advent-of-code-data to fetch input data or example data
    https://github.com/wimglenn/advent-of-code-data/
    pip install advent-of-code-data
"""
from aocd.models import Puzzle
from typing import List
import re

class Rule:
    key: str
    operator: str
    value: int
    dest: str

    def __init__(self, key, operator, value, dest):
        self.key = key
        self.operator = operator
        self.value = value
        self.dest = dest.lstrip(':') if dest else None

    def verify_rule(self, check_value):
        operators = {
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y
        }
        return self.dest if operators[self.operator](check_value, self.value) else None

    def get_ranges(self, start: int, end: int):

        if self.operator == '<':
            valid_range = (start, self.value - 1)
            invalid_range = (self.value, end)
        else: # operator == '>'
            valid_range = (self.value + 1, end)
            invalid_range = (start, self.value)
        return valid_range, invalid_range

class WorkFlow:
    id: str
    rules: List[Rule]
    default_workflow: str

    def __init__(self, input: str):
        id, rules = input.split('{')
        self.id = id
        self.rules, self.default_workflow = self.parse_rules(rules.rstrip('}'))

    def parse_rules(self, rules_str):
        parts = rules_str.split(',')
        rules = []
        for rule in parts[:-1]: # last part is default
            match = re.match(r'(\w)([<>=])(\d+)(:\w+)?', rule)
            if match:
                key, operator, value, dest = match.groups()
                rules.append(Rule(key, operator, int(value), dest))

        return rules, parts[-1]  # last part is the default workflow

    def verify_part(self, part):
        for rule in self.rules:
            part_value = getattr(part, rule.key)
            if dest := rule.verify_rule(part_value):
                return dest
        return self.default_workflow

class Part:
    x: int
    m: int
    a: int
    s: int
    part_value: int

    def __init__(self, input: str):
        parts = input.strip('{}').split(',')
        _value_sum = 0
        # store each part as values
        for part in parts:
            key, value = part.split('=')
            _value_sum += int(value)
            setattr(self, key, int(value))
        # store total value for part
        self.part_value = _value_sum

    def __repr__(self):
        return f'x={self.x}, m={self.m}, a={self.a}, s={self.s}, total={self.part_value}'


def parse_data(input_data):
    wf_raw, parts_raw = input_data.split('\n\n')
    wf = {w.split('{')[0]: WorkFlow(w) for w in wf_raw.split('\n')}
    parts = [Part(p) for p in parts_raw.split('\n')]

    return wf, parts

def process_parts(part, workflows, start_workflow):
    # part 1
    current_workflow = start_workflow

    while True:
        next_workflow = workflows[current_workflow].verify_part(part)
        if next_workflow in ('A', 'R'):
            return next_workflow
        else:
            current_workflow = next_workflow

def get_accepted_part_combinations(ranges, wf, current_workflow):
    # part 2
    if current_workflow == 'R':
        return 0
    if current_workflow == 'A':
        # calculate combinations
        res = 1
        for start, end in ranges.values():
            res *= end - start + 1
        return res

    total = 0
    is_condition_impossible = False
    for rule in wf[current_workflow].rules:

        start, end = ranges[rule.key]  # range for rule key, at start 1 - 4000

        valid_range, invalid_range = rule.get_ranges(start, end)

        if valid_range[0] <= valid_range[1]:
            ranges_copy = dict(ranges)
            ranges_copy[rule.key] = valid_range
            total += get_accepted_part_combinations(ranges_copy, wf, rule.dest)

        if invalid_range[0] <= invalid_range[1]:
            ranges[rule.key] = invalid_range
        else:
            is_condition_impossible = True
            break

    if not is_condition_impossible:
        total += get_accepted_part_combinations(ranges, wf, wf[current_workflow].default_workflow)

    return total

def part1(wf, parts) -> int:
    # store all parts that ends in 'A'
    A = [part for part in parts if process_parts(part, wf, 'in') == 'A']
    return sum(p.part_value for p in A)

def part2(wf) -> int:

    ranges = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }

    return get_accepted_part_combinations(ranges, wf, 'in')

def solve_puzzle(year: int, day: int, use_example_data: bool = False) -> None:

    puzzle = Puzzle(year, day)

    if use_example_data:
        print('using example data:')
        wf, parts = parse_data(puzzle.examples[0].input_data)
    else:
        wf, parts = parse_data(puzzle.input_data)

    print(f'Part 1: {part1(wf, parts)}')
    print(f'Part 2: {part2(wf)}')


if __name__ == '__main__':

    solve_puzzle(year=2023, day=19, use_example_data=False)
