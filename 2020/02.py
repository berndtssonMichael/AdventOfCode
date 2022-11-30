import pathlib

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):
    # 1-3 a: abcde
    # 1-3 b: cdefg
    # 2-9 c: ccccccccc
    data = []
    with open(file, 'r') as f:
        line = f.readline().strip()
        while line:
            p1, p2, p3 = line.split()
            count = [int(i) for i in p1.split('-')]
            char = p2[0]
            password = p3
            data.append([count, char, password])

            line = f.readline().strip()
    return data

def validate_password(count, char, password):
    # print('count', password.count(char), count[0], count[1])
    return count[0] <= password.count(char) <= count[1]

def validate_password_b(count, char, password):
    # get specific chars from password
    check_char = password[count[0] - 1] + password[count[1] - 1]
    return check_char.count(char) == 1

def solve_a(data):
    return sum([validate_password(row[0], row[1], row[2]) for row in data])

def solve_b(data):
    return sum([validate_password_b(row[0], row[1], row[2]) for row in data])

def main():

    data = parse(INPUT_DIR / '02.txt')
    # data = parse(INPUT_DIR / 'test.txt')

    print(f'Answer A: {solve_a(data)}')

    print(f'Answer b: {solve_b(data)}')


if __name__ == '__main__':
    main()
