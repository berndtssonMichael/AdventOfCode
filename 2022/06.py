
signal = open('input/06.txt', 'r').read().strip()

def get_start_pos(st, pos):
    chars = len(st)
    for i in range(chars - pos - 1):
        if len(set(st[i:i + pos])) == pos:
            return pos + i

print(f'A: {get_start_pos(signal, 4)}')
print(f'B: {get_start_pos(signal, 14)}')
