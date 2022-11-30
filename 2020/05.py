import pathlib
import re

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):
    input_data = [line.strip() for line in open(file, 'r').readlines()]
    
    return input_data

def calc_seat(data):
    # first 7 char
    # F means to take the lower half, keeping rows 0 through 63.
    # B means to take the upper half, keeping rows 32 through 63.

    # # last 3 char
    # R means to take the upper half, keeping columns 4 through 7.
    # L means to take the lower half, keeping columns 4 through 5.

    # each seat could be converted to binary value
    # map B = 1, F = 0, R = 1, L = 0

    # seat_id = ''.join(c for c in data)
    # lookup = {'B': '1', 'F': '0', 'R': '1', 'L': '0',}

    # seat_id = int(''.join(lookup[c] for c in data), 2)
    # print('seat:', seat_id)

    # but hear we try to do the logic as described
    no_of_rows = 128
    mid_row = no_of_rows / 2
    no_of_cols = 8
    mid_col = no_of_cols / 2
    row_data = data[:7]
    col_data = data[7:]
    # print(row_data)
    # print(col_data)

    row = 0
    col = 0
    for r in row_data:
        if r == 'B': # higher
            row += mid_row
            mid_row /= 2
        else:
            mid_row /= 2
    # print('row', row)

    for c in col_data:
        if c == 'R':
            col += mid_col
            mid_col /= 2
        else:
            mid_col /= 2
    # print('col', col)
    return int(row * 8 + col)

def solve_a(data):
    #
    return(max([
        calc_seat(seat) for seat in data
    ]))

def solve_b(data):
    seats = sorted([calc_seat(seat) for seat in data])

    my_seat = [s + 1 for s in seats if s + 1 not in seats][0]
    return my_seat



def main():

    # data = parse(INPUT_DIR / 'test.txt')
    data = parse(INPUT_DIR / '05.txt')
    # print(data)
    # data = ['FBFBBFFRLR']
    print(f'Answer A: {solve_a(data)}')

    print(f'Answer B: {solve_b(data)}')


if __name__ == '__main__':
    main()
