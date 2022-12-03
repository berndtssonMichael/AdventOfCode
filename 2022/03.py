import string

bags = [v.split()[0] for v in open('input/03.txt', 'r').readlines()]

print(sum(
        string.ascii_letters.index(
            set(bag[:len(bag) // 2]).intersection(set(bag[len(bag) // 2:])).pop()) + 1
        for bag in bags
))

print(sum(
        string.ascii_letters.index(
            set(bags[i]).intersection(set(bags[i + 1]), set(bags[i + 2])).pop()) + 1
        for i in range(0, len(bags), 3)
))
