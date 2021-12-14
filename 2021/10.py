from os import path
from time import perf_counter

t1_start = perf_counter()
print()

input_file = path.relpath('input/10.txt')

lines = [l.strip() for l in open(input_file).readlines()]

points_endings = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points_closing = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']
MATCH_O_C = [(o, c) for o, c in zip(OPENING, CLOSING)]


def is_line_corrupt(line):
    # check if line is corrupt
    # if True, return missing closing char
    # else return False
    stack=[]
    for char in line:
        if char in OPENING:
            stack.append(char)
        else:
            last_open = stack.pop()
            if (last_open, char) not in MATCH_O_C:
                return char
    return False


def get_missing_closings(line):
    # returns a list of missing closing
    # assume line not corrupted
    stack=[]
    for char in line:
        if char in OPENING:
            stack.append(char)
        else:
            last_open = stack[-1:][0]
            if (last_open, char) in MATCH_O_C:
                stack.pop()
    # revers stack and map to closing
    res = [CLOSING[OPENING.index(c)] for c in stack[::-1]]
    return res


def calc_points_for_missing_closings(line):
    # return calculated sum of points
    points = 0
    for c in line:
        points = points * 5 + points_closing[c]
    return points



# SOLVE A
endings = []
corrupted_lines = [] # store lines to exclude in B
for row, line in enumerate(lines):
    e = is_line_corrupt(line)
    if e:
        endings.append(e)
        corrupted_lines.append(row)

# map missing endings to points an sum it up
print(f'Answer A: {sum([points_endings[c] for c in endings])}')


# SOLVE B
# use corrupted_lines from A
final_sum = []
for row, line in enumerate(lines):
    if row not in corrupted_lines:
        e = get_missing_closings(line)
        if e:
            final_sum.append(calc_points_for_missing_closings(e))

final_sum.sort()

print(f'Answer B: {final_sum[(mid:=len(final_sum)//2):mid+1][0]}')

print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
