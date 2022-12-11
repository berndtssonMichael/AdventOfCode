from collections import deque
from math import prod

class Monkey():
    def __init__(self, items, op, divide, send_true, send_false):
        self.items = deque(items)
        self.op = op
        self.divide = divide
        self.send_true = send_true
        self.send_false = send_false
        self.count_inspections = 0

    def __repr__(self):
        return f'items: {self.items}, inspections: {self.count_inspections}'

    def inspect(self, div_func):
        # div_func: lambda for handle worry level
        # lambda x: x // 3
        # lambda x: x % prod of all divide
        while self.items:
            self.count_inspections += 1
            item = self.items.popleft()
            item = div_func(self.op(item))
            self.pass_item(item)

    def add_item(self, item):
        self.items.append(item)

    def pass_item(self, item):
        if item % self.divide == 0:
            monkeys[self.send_true].add_item(item)
        else:
            monkeys[self.send_false].add_item(item)


def create_monkeys(test=False):
    if test:
        monkeys = [
            Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
            Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
            Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
            Monkey([74], lambda x: x + 3, 17, 0, 1),
        ]
    else:
        monkeys = [
            Monkey([54, 89, 94], lambda x: x * 7, 17, 5, 3),
            Monkey([66, 71], lambda x: x + 4, 3, 0, 3),
            Monkey([76, 55, 80, 55, 55, 96, 78], lambda x: x + 2, 5, 7, 4),
            Monkey([93, 69, 76, 66, 89, 54, 59, 94], lambda x: x + 7, 7, 5, 2),
            Monkey([80, 54, 58, 75, 99], lambda x: x * 17, 11, 1, 6),
            Monkey([69, 70, 85, 83], lambda x: x + 8, 19, 2, 7),
            Monkey([89], lambda x: x + 6, 2, 0, 1),
            Monkey([62, 80, 58, 57, 93, 56], lambda x: x * x, 13, 6, 4),
        ]
    return monkeys

def solve_a(monkeys):
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect(lambda x: x // 3)

    inspections = sorted([monkey.count_inspections for monkey in monkeys])
    return(inspections[-2:][0] * inspections[-2:][1])

def solve_b(monkeys):
    # create modulus factor by getting the product of all divide values
    mod = prod(m.divide for m in monkeys)

    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect(lambda x: x % mod)
    inspections = sorted([monkey.count_inspections for monkey in monkeys])
    return(inspections[-2:][0] * inspections[-2:][1])


monkeys = create_monkeys(False)
print(f'A: {solve_a(monkeys)}')

monkeys = create_monkeys(False)
print(f'B: {solve_b(monkeys)}')
