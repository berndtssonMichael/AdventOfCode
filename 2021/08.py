from os import path
from itertools import permutations
from time import perf_counter
t1_start = perf_counter()

input_file = path.relpath('input/08.txt')

# This solution is painfully slow

numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


# uniq len: number
uniq = {2: 1, 3: 7, 4: 4, 7: 8}
count_a = 0
count_b = 0
# read file and solve A
with open(input_file) as f:
    line = f.readline().strip()
    while line:
        input, output = map(lambda part: part.split(), line.split('|'))
        count_a += sum(len(c) in uniq.keys() for c in output)

        for p in permutations("abcdefg"):
            trans = str.maketrans("abcdefg", "".join(p))
            a = ["".join(sorted(w.translate(trans))) for w in input]
            if all(w in numbers for w in a):
                b = ["".join(sorted(w.translate(trans))) for w in output]
                count_b += int("".join(str(numbers[w]) for w in b))

        line = f.readline().strip()


print(f'result A: {count_a}')
print(f'result B: {count_b}')

# print(f'result B: {len(count_b)}')
print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
