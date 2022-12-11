values = [1] # add initial values

with open('input/10.txt') as fp:
    for line in fp:
        v = line.strip()[5:]
        if v == '':
            values.append(0)
        else:
            values.extend([0, int(v)])


def solve_a(values):
    signal = 0
    for i in range(20, 221, 40):
        signal += i * sum(values[:i])
    return signal


def solve_b(values):

    # create empty screen
    screen_rows = 6
    screen_width = 40
    screen = [['-' for _ in range(screen_width)] for _ in range(screen_rows)]

    running_pos = 0
    for row in screen:
        for pos in range(len(row)):
            x = sum(values[:running_pos + 1])
            sprite = [x - 1, x, x + 1]
            row[pos] = '#' if pos in sprite else '.'
            running_pos += 1

    return screen

print(f'A: {solve_a(values)}')

# part B
screen = solve_b(values)
print('B:')
for row in screen:
    print(''.join(row))
