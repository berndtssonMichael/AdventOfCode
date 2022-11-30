import pathlib

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):
    numbers = set([int(v.strip()) for v in open(file, 'r').readlines()])
    return numbers

def solve_a(nums, search_for):
    for i in nums:
        if search_for - i in nums:
            print('A: ', i, search_for - i, i * (search_for - i))
            return

def solve_b(nums, search_for):
    for a in nums:
        for b in nums:
            if search_for - a - b in nums:
                print('B: ', a, b, search_for - a - b, a * b * (search_for - a - b))
                return

def main():
    FIND = 2020

    numbers = parse(INPUT_DIR / '01.txt')
    solve_a(numbers, FIND)
    solve_b(numbers, FIND)

if __name__ == '__main__':
    main()
