pairs = [v.strip().split(',')
    for v in open('input/04.txt', 'r').readlines()]

part_a, part_b = 0, 0
for v in pairs:
    p1, p2 = v[0].split('-'), v[1].split('-')

    s1 = set(range(int(p1[0]), int(p1[1]) + 1))
    s2 = set(range(int(p2[0]), int(p2[1]) + 1))
    # check A
    if any([s1.issubset(s2), s2.issubset(s1)]):
        part_a += 1
    # check B
    if not any([s1.isdisjoint(s2), s2.isdisjoint(s1)]):
        part_b += 1

print(f'A: {part_a}')
print(f'B: {part_b}')

# A: 571
# B: 917
