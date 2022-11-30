import pathlib
from collections import defaultdict

# define data-file
ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2020' / 'input'


def parse(file):
    input_data = [line.strip() for line in open(file, 'r').readlines()]

    return input_data

def group_answers_a(input_data):
    groups = []
    answer = set()
    for line in input_data:
        line = line.rstrip()
        if not line:
            if answer:
                groups.append(answer)
            answer = set()
        else:
            for c in line:
                answer.add(c)

    groups.append(answer)

    return groups

def filter_answers(dict, persons):
    return {k: v for k, v in dict.items() if v == persons}


def group_answers_b(input_data):
    groups = []
    answer = defaultdict(int)
    persons = 0
    for line in input_data:
        line = line.rstrip()
        if not line:
            if answer:
                answer = filter_answers(answer, persons)
                groups.append(answer)
            answer = defaultdict(int)
            persons = 0
        else:
            persons += 1
            for c in line:
                answer[c] += 1

    answer = filter_answers(answer, persons)
    groups.append(answer)

    return groups

def count_answers(data):
    return(len(data))

def solve_a(data):
    data = group_answers_a(data)
    return sum([count_answers(answers) for answers in data])


def solve_b(data):
    data = group_answers_b(data)
    return sum([count_answers(answers) for answers in data])


def main():

    # data = parse(INPUT_DIR / 'test.txt')
    data = parse(INPUT_DIR / '06.txt')
    # print(data)
    print(f'Answer A: {solve_a(data)}')

    print(f'Answer B: {solve_b(data)}')


if __name__ == '__main__':
    main()
