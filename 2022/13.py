import json
from itertools import zip_longest
# (list1, list2, fillvalue = None)

def parse(filename):
    signals = []
    for pairs in open(filename).read().strip().split("\n\n"):
        p1, p2 = pairs.split('\n')
        signals.append((json.loads(p1), json.loads(p2)))
    return signals

packets = {
    i: (eval(p[0]), eval(p[1]))
    for i, p in enumerate([p.splitlines() for p in open("input/test.txt").read().split("\n\n")], 1)
}

print(packets)



def compare(left, right):
    # a negative return is a ok pair
    if isinstance(left, int) and isinstance(right, int):
        return left - right  # if positive pair is not OK

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right, fillvalue=None):
            if l is None:
                return -1
            if r is None:
                return 1
            check = compare(l, r)
            if check != 0:
                return check
        return 0

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare(left, right)

def solve_a(signals):
    sum_ok_pairs = 0
    ok_pairs = []
    cnt = 0
    for left, right in signals:
        cnt += 1
        if compare(left, right) < 0:
            sum_ok_pairs += cnt
            ok_pairs.append(cnt)
    # print(ok_pairs)
    return sum_ok_pairs


# signals = parse('input/test.txt')
signals = parse('input/13.txt')
print(f'A: {solve_a(signals)}')
