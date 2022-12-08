from numpy import prod
grid = [[int(v) for v in line.strip()] for line in open('input/08.txt', 'r').readlines()]

def get_score(check, trees):
    tree_count = 0
    for tree in trees:
        tree_count += 1
        if tree >= check:
            break
    return tree_count

def solve(grid):
    count = 0
    scores = []

    row_len = len(grid)
    col_len = len(grid[0])

    for row in range(row_len):
        for col in range(col_len):

            # what to check
            check_value = grid[row][col]
            # check against
            left = list(grid[row][:col])
            right = list( grid[row][col + 1:])
            up = [v[col] for v in grid[:row]]
            down = [v[col] for v in grid[row + 1:]]

            # Part A
            # handle outer edge
            if 0 in (row, col) or row == row_len - 1 or col == col_len - 1:
                count += 1
            else:
                if (
                    all(v < int(check_value) for v in left)
                    or all(v < int(check_value) for v in right)
                    or all(v < int(check_value) for v in up)
                    or all(v < int(check_value) for v in down)
                ):
                    count += 1

            # Part B
            points = [
                get_score(check_value, reversed(left)),
                get_score(check_value, right),
                get_score(check_value, reversed(up)),
                get_score(check_value, down)
            ]
            scores.append(prod(points))

    return count, max(scores)

a, b = solve(grid)
print(f'A: {a}')
print(f'B: {b}')
