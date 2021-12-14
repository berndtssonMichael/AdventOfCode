from time import perf_counter
import pathlib
from collections import defaultdict

ROOT_DIR = pathlib.Path(__file__).parent.parent
input_file = ROOT_DIR / '2021/input/13.txt'


t1_start = perf_counter()

# fetch data
input_data = [line.strip() for line in open(input_file).readlines()]

fold_instructions_from = input_data.index('') 

coords = set()
for r in input_data[:fold_instructions_from]:
    x, y = r.split(',')
    coords.add((int(x), int(y)))


fold_instructions = []
for r in input_data[fold_instructions_from + 1:]:
    _, _, fold = r.split()
    direction, step = fold.split('=')
    fold_instructions.append((direction, int(step)))


def fold_paper(fold):
    # filter out set after folding
    if fold[0] == 'y':
        move_x = 0
        move_y = fold[1]
        filter_expr = [c for c in coords if c[1] > move_y]
    else:
        move_x = fold[1]
        move_y = 0
        filter_expr = [c for c in coords if c[0] > move_x]
    for coord in filter_expr:
        _x, _y = coord  # current x, y position
        x = _x - (_x - move_x) * 2 if move_x > 0 else _x
        y = _y - (_y - move_y) * 2 if move_y > 0 else _y
        coords.discard(coord)

        if x >= 0 and y >= 0:
            coords.add((x, y))


# solve A
fold_paper(fold_instructions[0])
print(f'Answer A:{len(coords)}')

# continue to fold and solve B
for fold in fold_instructions[1:]:
    fold_paper(fold)

# create matrix to se letters
matrix = []
for row in range(max(c[1] for c in coords)+1):
    _row = []
    for col in range(max(c[0] for c in coords)+1):
        _row.append('#' if (col, row) in coords else ' ')
    matrix.append(_row)
print()
print('Answer for B:')
# LGHEGUEJ

for r in matrix:
    print(''.join(r))

print()




t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
