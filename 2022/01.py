from os import path

# input_file = path.relpath('input/01.txt')
input_file = path.relpath('input/test.txt')
# read all values
values = [v.strip() for v in open(input_file, 'r').readlines()]

def group_meals(values):
    calories = []
    s = 0
    for v in values:
        if v.isdigit():
            s += int(v)
        else:
            calories.append(s)
            s = 0
    # add last item
    calories.append(s)

    return calories

def solve_part1(values):
    calories = group_meals(values)
    return(max(calories))

def solve_part2(values):
    calories = group_meals(values)

    calories.sort(reverse=True)
    return sum(calories[:3])

print(f'answer part 1: {solve_part1(values)}')
print(f'answer part 2: {solve_part2(values)}')
