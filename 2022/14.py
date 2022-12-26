
def get_data():
    input = [l.strip('\n') for l in open('input/14.txt').readlines()]
    return input


def create_start_cave(input):
    cave = set()

    for line in input:
        points = [tuple(map(int, p.split(','))) for p in line.split(' -> ')]
        for i in range(len(points) - 1):
            # p1, p2 = Point(*points[i]) , Point(*points[i + 1])
            # col_range = range(min(p1.col, p2.col), max(p1.col, p2.col) + 1)
            # row_range = range(min(p1.row, p2.row), max(p1.row, p2.row) + 1)
            p1, p2 = points[i] , points[i + 1]
            col_range = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            row_range = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)

            cave.update(((col, row) for col in col_range for row in row_range))

    return cave


def solve_a():
    cave = create_start_cave(get_data())
    cave_bottom = max(row for _, row in cave)

    cnt = 0
    start_col, start_row = 500, 0  # starting point
    col, row = start_col, start_row
    while True:
        if (col, row) in cave:  # try again from begining
            col, row = start_col, start_row
        if row >= cave_bottom:
            break
        # down
        if (col, row + 1) not in cave:
            row += 1
        # left
        elif (col - 1, row + 1) not in cave:
            col, row = col - 1, row + 1
        # right
        elif  (col + 1, row + 1) not in cave:
            col, row = col + 1, row + 1
        # stop
        else:
            cnt += 1
            cave.add((col, row))  # expand cave
    return cnt


def solve_b():
    cave = create_start_cave(get_data())
    cave_bottom = max(row for _, row in cave) + 1

    cnt = 0
    start_col, start_row = 500, 0  # starting point
    col, row = start_col, start_row
    while True:
        if (col, row) in cave:  # try again from begining
            col, row = start_col, start_row
        # down
        if (col, row + 1) not in cave and row < cave_bottom:
            row += 1
        # left
        elif (col - 1, row + 1) not in cave and row < cave_bottom:
            col, row = col - 1, row + 1
        # right
        elif  (col + 1, row + 1) not in cave and row < cave_bottom:
            col, row = col + 1, row + 1
        # stop
        else:
            cnt += 1
            cave.add((col, row))  # expand cave
        if (col, row) == (start_col, start_row):
            break
    return cnt

print(f'Answer A: {solve_a()}')
print(f'Answer B: {solve_b()}')
