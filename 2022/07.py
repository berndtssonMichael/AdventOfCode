from collections import defaultdict

lines = [v.strip() for v in open('input/07.txt', 'r').readlines()]

def get_dir_size(lines) -> defaultdict:
    path = []
    dirs = defaultdict(int)
    for line in lines:
        size = 0
        if line == '$ cd ..':
            path.pop() # back one step
        elif line.startswith('$ cd'):
            dir = line[5:]
            path.append(dir)
        elif line[0].isnumeric(): # found a file
            size = line.split()[0]
            string_path = ''
            for folder in path:
                string_path += folder
                dirs[string_path] += int(size)
    return dirs

def solve_a(lines):
    dirs = get_dir_size(lines)
    return sum(s for s in dirs.values() if s <= 100000)

def solve_b(lines):
    dirs = get_dir_size(lines)

    TOTALSIZE, NEEDSPACE = 70000000, 30000000
    space_to_free = NEEDSPACE - (TOTALSIZE - dirs['/'])
    return min([v for v in dirs.values() if v >= space_to_free])

print(f'A: {solve_a(lines)}')
print(f'B: {solve_b(lines)}')
