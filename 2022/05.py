from collections import defaultdict

def read_file():
    stacks, moves = open('input/05.txt', 'r').read().split('\n\n')

    stacks = list(reversed(stacks.split('\n')))  # reversed list of stacks
    cols = stacks.pop(0)  # fetch columns
    no_of_cols = int(max(cols.split()))  # calc number of columns

    # create index to use in string, assuming all strings are the same length
    col_idx = {i + 1: x for (i, x) in enumerate(range(1, no_of_cols * 4 - 1, 4))}

    columns = defaultdict(list)

    # create columns
    for stack in stacks:
        # make all stacks equally long
        s = stack.ljust(no_of_cols * 4)[:no_of_cols * 4 - 1]
        for idx, pos in col_idx.items():
            if s[pos] != ' ':
                columns[idx].append(s[pos])

    # create list of move directions
    moves = moves.split('\n')
    move_directions = []
    for move in moves:
        l = [int(i) for i in move.split() if i.isnumeric()]
        if l:
            move_directions.append(l)

    return columns, move_directions

def solve(columns, move_directions, cratemover_9001=False):
    # rearrange columns
    for move in move_directions:
        items, move_from, move_to = move[0], move[1], move[2]
        remove_items = len(columns[move_from]) - items
        in_transit = columns[move_from][remove_items:]
        if not cratemover_9001:
            in_transit = reversed(in_transit)

        columns[move_to].extend(in_transit)
        columns[move_from] = columns[move_from][:-items]
    return ''.join([col[-1] for col in columns.values()])

columns, move_directions = read_file()
print(f'A: {solve(columns, move_directions)}')
columns, move_directions = read_file()
print(f'V: {solve(columns, move_directions, True)}')
