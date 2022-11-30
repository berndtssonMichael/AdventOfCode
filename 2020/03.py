import pathlib
import numpy as np
# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):

    # convert map to 0 for open space and 1 for trees
    data = [[0 if d == '.' else 1 for d in l.strip()] for l in open(file).readlines()]

    #store as numpy arrays
    matrix = np.array(data)
    return matrix

def expand_matrix(matrix, step_right, step_down):
    rows, cols = np.shape(matrix)
    expand_cols = int((rows * step_down * step_right)  / cols) + 1
    # expand_rows = int((rows * step_right * step_down)  / rows) + 1
    # rows
    _matrix = np.concatenate([matrix for _ in range(expand_cols)], axis=1)
    # cols
    # _matrix = np.concatenate([matrix for _ in range(expand_rows)], axis=0)
    return _matrix



def count_trees(matrix, step_right, step_down):
    # print('size', *np.shape(matrix))
    # expand matrix no correct size
    _matrix = expand_matrix(matrix, step_right, step_down)
    # print('size 2', *np.shape(_matrix))

    # create positions
    rows, _ = np.shape(_matrix)
    x = 0
    y = 0
    coords = []

    while y < rows:
        coords.append([y, x])
        x += step_right
        y += step_down

    # print(coords)

    trees = 0
    for c in coords:
        trees += _matrix[c[0], c[1]]
    return trees

def solve_a(data):
    return count_trees(data, step_right=3, step_down=1)

def solve_b(matrix):
    # step_right, step_down
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    trees = []
    for slope in slopes:
        trees.append(count_trees(matrix, step_right=slope[0], step_down=slope[1]))
    prod = None
    for i in trees :
        if prod is None:
            prod = float(i)
        else:
            prod *= float(i)
    return prod



def main():

    matrix = parse(INPUT_DIR / '03.txt')
    # matrix = parse(INPUT_DIR / 'test.txt')

    print(f'Answer A: {solve_a(matrix)}')

    print(f'Answer B: {solve_b(matrix)}')


if __name__ == '__main__':
    main()
