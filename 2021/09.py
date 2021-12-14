from os import path
from time import perf_counter
import math

t1_start = perf_counter()
print()
input_file = path.relpath('input/09.txt')

# create matrix from file
matrix = [[int(d) for d in l.strip()] for l in open(input_file).readlines()]
no_of_rows = len(matrix)
no_of_cols = len(matrix[0])

def whos_my_neighbours(coord: tuple) -> list:
    # return list of neighbours coordinates
    x, y = coord
    cos = []
    if x > 0 :
        cos.append((x-1, y))
    if x + 1 < no_of_rows :
        cos.append((x+1, y))
    if y > 0:
        cos.append((x, y-1))
    if y + 1 < no_of_cols:
        cos.append((x, y+1))
    return cos

def check_neighbour_value(coord: tuple) -> int:
    
    return matrix[coord[0]][coord[1]]

def check_if_smaller_than_neighbours(coord: tuple) -> int:
    """
        check all values around x, y
        if the value in x, y (base_value) is lower than all neighbours
        return base_value
        else return -1

    """
    base_value = check_neighbour_value(coord) # value to compare with
    neighbours = whos_my_neighbours(coord)
    neighbours_value = []
    for neighbour in neighbours:
        neighbours_value.append(check_neighbour_value(neighbour))
            #matrix[neighbour[0]][neighbour[1]])
    if base_value < min(neighbours_value):
        return base_value
    return -1


res_dict = {}
# store all low points in dict with it's coordinates as key
# comes in handy when solving B
res_dict = {(x, y): c for x in range(no_of_rows) for y in range(no_of_cols) if (c:=check_if_smaller_than_neighbours((x, y))) >= 0}

print(f'Answer A: {sum([x+1 for x in res_dict.values()])}')

# part B
# res_dict includes all low points and it's coordinats
# use that to check for basins

def check_neighbours(coord: tuple, exclude: list) -> list:

    base_value = check_neighbour_value(coord) #matrix[x][y]
    neighbours = whos_my_neighbours(coord)
    list_of_pos = []
    for neighbour in neighbours:
        if (v:=check_neighbour_value(neighbour)) > base_value and v < 9 and neighbour not in exclude:
            list_of_pos.append(neighbour)
    return list_of_pos


# create all basins
is_checked = []  # store already checked positions, since no position is allowed in multiple basins
basins = {}      # dict to store basins, values == coordinats
for ix, c in enumerate(res_dict.keys()):
    positions = [c] # add starting coordinate
    for p in positions:
        _res = check_neighbours(p, is_checked) # returns a list
        positions += _res   # add new result to positions
        is_checked += _res  # add new result to exclude_list so we dont check it again
    basins[ix] = positions


# order result
ordered_result = [i for i in sorted([len(i) for i in basins.values()])]

# print out answer
print(f'Answer B: {math.prod(ordered_result[-3:])}')
print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
