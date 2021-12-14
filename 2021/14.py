from time import perf_counter
import pathlib
from collections import defaultdict


ROOT_DIR = pathlib.Path(__file__).parent.parent
input_file = ROOT_DIR / '2021/input/14.txt'


t1_start = perf_counter()

# fetch data
input_data = [line.strip() for line in open(input_file).readlines()]

template = [c for c in input_data[0]]
# print('template', template)

# which combination adds which char?
# pairs = {
#    'CH': 'B',
#    'HH': 'N'
# }
pairs = {k: v for k, v in [r.split(' -> ') for r in input_data[2:]]}

def init_pair_count(template):
    pair_count = defaultdict(int)
    for i in range(len(template)-1):
        pair_count[template[i]+template[i+1]] += 1
    return pair_count

def evolve(pair_count):
    new_pair_count = defaultdict(int)

    # for each existing pair create new
    # first char in pair + new char
    # new char + second char in pair
    for k, v in pair_count.items():
        new_pair_count[k[0]+pairs[k]] += v
        new_pair_count[pairs[k]+k[1]] += v
    return new_pair_count

def calc_answer(pair_count): 
    # count each char in existing pairs
    no_of_chars = defaultdict(int)
    # add extra count for first and last char
    no_of_chars[template[1]] += 1
    no_of_chars[template[-1]] += 1
    for k, v in pair_count.items():
        no_of_chars[k[0]] += v  # first char
        no_of_chars[k[1]] += v  # second char

    # each char exists twice, hence // 2
    sort_list = [v//2 for v in sorted(no_of_chars.values(), reverse=True)]

    return sort_list[0] - sort_list[-1]

# Solve A
STEPS = 10
pair_count = init_pair_count(template)
for step in range(STEPS):
    pair_count = evolve(pair_count)
print(f'Answer A: {calc_answer(pair_count)}')


# Solve B
STEPS = 40
pair_count = init_pair_count(template)
for step in range(STEPS):
    pair_count = evolve(pair_count)
print(f'Answer B: {calc_answer(pair_count)}')

print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
