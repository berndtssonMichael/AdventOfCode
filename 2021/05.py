from os import path
from time import perf_counter
t1_start = perf_counter()

input_file = path.relpath('input/05.txt')

# create empty result array
grid_size = 1000
res_a = [[0 for y in range(grid_size)] for x in range(grid_size)]
res_b = [[0 for y in range(grid_size)] for x in range(grid_size)]


def update_res(p1, p2, question='a'):
    assert question in['a', 'b']
    # if question == 'a' and not (p1.y == p2.y or p1.x == p2.x):
    if question == 'a' and not (p1[0] == p2[0] or p1[1] == p2[1]):
        return
    if question == 'a':
        _arr = res_a
    else:
        _arr = res_b 

    sign_x = -1 if p1[0] > p2[0] else 1
    sign_y = -1 if p1[1] > p2[1] else 1

    x_cord = list(range(p1[0], p2[0] + sign_x, sign_x))
    y_cord = list(range(p1[1], p2[1] + sign_y, sign_y))

    if len(x_cord) == 1:
        x_cord = x_cord * len(y_cord)
    elif len(y_cord) == 1:
        y_cord = y_cord * len(x_cord)

    # get coordinate and update array
    for x, y in zip(x_cord, y_cord):
        _arr[y][x] += 1


# read file and update result array
with open(input_file) as f:
    line = f.readline().strip()
    while line:
        _row = line.replace(' -> ', ',').split(',')
        update_res((int(_row[0]), int(_row[1])), (int(_row[2]), int(_row[3])), 'a')
        update_res((int(_row[0]), int(_row[1])), (int(_row[2]), int(_row[3])), 'b')
        line = f.readline().strip()

# sum res A
count_a = [val for row in res_a for val in row if val >= 2]

print(f'result A: {len(count_a)}')

# sum res B
count_b = [val for row in res_b for val in row if val >= 2]

print(f'result B: {len(count_b)}')
print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
