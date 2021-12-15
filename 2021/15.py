
import pathlib
import numpy
import heapq
from time import perf_counter

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
input_file = ROOT_DIR / '2021/input/15.txt'

t1_start = perf_counter()

# create numpy array from file, remove 1 from each risklevel
matrix = numpy.genfromtxt(input_file, dtype=int, delimiter=1) - 1


def calc_risk_level(data):
    max_row, max_col = numpy.shape(data)  # size of grid
    risk_levels = [(0, (0, 0))]  # risk, starting point
    while risk_levels:
        # remove smallest item, i.e lowest risk
        risk, (col, row) = heapq.heappop(risk_levels)
        # when we reach end of matrix return risk
        if (col, row) == (max_col - 1, max_row - 1):
            return risk
        for col, row in [
            (col, row + 1), (col + 1, row), (col, row - 1), (col - 1, row)
        ]:
            if (col >= 0 and col < max_col and row >= 0 and row < max_row
                    and data[row][col] >= 0):
                heapq.heappush(
                        risk_levels,
                        (risk + (data[row][col] % 9) + 1, (col, row))
                )
                data[row][col] = -1    # mark as seen


matrix_b = matrix.copy()  # store copy of original matrix before solving a
print(f'Answer B: {calc_risk_level(matrix)}')

# expand numpy array
matrix_b = numpy.concatenate([matrix_b + i for i in range(5)], axis=0)
matrix_b = numpy.concatenate([matrix_b + i for i in range(5)], axis=1)
print(f'Answer B: {calc_risk_level(matrix_b)}')


t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
