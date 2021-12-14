from os import path
from collections import namedtuple
from time import perf_counter


t1_start = perf_counter()
input_file = path.relpath('input/11.txt')
input = [[int(d) for d in l.strip()] for l in open(input_file, 'r').readlines()]

NO_OF_ROWS = len(input)
NO_OF_COLS = len(input[0])

STEPS = 100

Coord = namedtuple('Coord', ['x', 'y'])

matrix = {Coord(x, y): input[x][y] for x in range(NO_OF_ROWS) for y in range(NO_OF_COLS)}


def print_coords(matrix, heading = '', print_key_value=False):
    # for debug purpose
    if heading:
        print()
    print(heading)
    if print_key_value:
        for k, v in matrix.items():
            print(k, v)
    else:
        for x in range(NO_OF_COLS):
            print(''.join([str(matrix[(x, y)]) for y in range(NO_OF_ROWS) ]))


def whos_my_neighbours(start_coord: Coord) -> list[Coord]:
    # return list of neighbours coordinates
    x, y = start_coord.x, start_coord.y
    neighbours = []      # should be a set - might be faster
    for _coord in [
        Coord(x - 1, y - 1),    Coord(x, y - 1),    Coord(x + 1, y - 1),
        Coord(x - 1, y),                            Coord(x + 1, y),
        Coord(x - 1, y + 1),    Coord(x, y + 1),    Coord(x + 1, y + 1)
    ]:
        if _coord in matrix.keys():
            neighbours.append(_coord)

    return neighbours

def update_neighbours(coords: list[Coord], flashing: set[Coord]) -> set[Coord]:
    for coord in coords:
        # check neighours for each coord
        neighbours = whos_my_neighbours(coord)
        for neighbour in neighbours:
            if neighbour not in flashing:
                v = matrix[neighbour]  # current value
                matrix[neighbour] = v+1 if v < 9 and v > 0 else 0  # update value or reset
                if v >= 9:  # will now light up
                    flashing.add(neighbour)
                    flashing = update_neighbours([neighbour], flashing)
    return flashing


# SOLVE A AND B
no_of_flashes = 0
all_flashing_at_step = 0
s = 1
# for s in range(STEPS):
while True:
    # increase all 1 step
    _flashes = []   # change to set()
    for k, v in matrix.items():
        if v == 9:
            _flashes.append(k)
        matrix[k] = v+1 if v < 9 else 0
    added = update_neighbours(_flashes, set(_flashes))

    now_flashing = len([v for v in matrix.values() if v ==0])
    if s <= STEPS:
        no_of_flashes += now_flashing

    if now_flashing == 100 and all_flashing_at_step == 0:
        all_flashing_at_step = s
        if s > STEPS:
            break
    s += 1  # increse step 

print()
print(f'Answer A: {no_of_flashes}')
print(f'Answer B: {all_flashing_at_step}')

print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
