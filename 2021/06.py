from os import path
from time import perf_counter
from collections import defaultdict

t1_start = perf_counter()

input_file = path.relpath('input/06.txt')
input = [int(v) for v in  [d.strip() for d in open(input_file).readlines()][0].split(',')]

NUM_OF_DAYS = 256

fishes = defaultdict(int)

# init fishes
for f in input:
    fishes[f] += 1

# iterate over days
for day in range(1, NUM_OF_DAYS + 1):
    _f = defaultdict(int) # new empty dict

    for k, v in fishes.items():
        if k == 0:
            # create new fishes and reset to 6
            _f[8] += v
            _f[6] += v
        else:
            _f[k-1] += v

    #fishes = dict(_f)
    fishes = _f

    if day == 80:
        print(f'A: after {day} days: {sum(fishes.values())}')


print(f'B: after {day} days: {sum(fishes.values())}')

t1_stop = perf_counter()
print()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
