from os import path
from time import perf_counter
from statistics import median

t1_start = perf_counter()

input_file = path.relpath('input/07.txt')
input = [int(v) for v in  [d.strip() for d in open(input_file).readlines()][0].split(',')]

def solve_a():
    med = int(median(input))
    return sum([abs(i - med) for i in input])

def solve_b():
    def fuelcost(step):
        return step * (step + 1) // 2

    def sumfuelcost(step):
        return sum(fuelcost(abs(i - step)) for i in input)

    return min(sumfuelcost(i) for i in range(min(input), max(input)+1))


print(f'A: {solve_a()}') # A: 341534
print(f'A: {solve_b()}') # B:  93397632


t1_stop = perf_counter()
print()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')