import pathlib
from collections import defaultdict
from time import perf_counter


ROOT_DIR = pathlib.Path(__file__).parent.parent
INPUT_DIR = ROOT_DIR / '2021/input'
input_file = INPUT_DIR / '12.txt'


# read file and create junctions
junctions = set()
with open(input_file) as f:
    line = f.readline().strip()
    while line:
        s, e = line.split('-')
        junctions.add((s, e))
        line = f.readline().strip()


# create connections
# dict[point] = set(connection points)
connections = defaultdict(set)
large_caves= set()

for s, e in junctions:
    connections[s].add(e)
    connections[e].add(s)
    if s.isupper():
        large_caves.add(s)
    if e.isupper():
        large_caves.add(e)


t1_start = perf_counter()


def can_visit_cave_again(visited):
    # used in part B to check if we can revisit
    return not any(v > 1 for v in visited.values())


def create_path(part = 'A'):

    cave_paths = []
    def _create_path(path = [], visited = defaultdict(int), point = 'start'):

        _path = path.copy()
        _path.append(point)

        new_visited = visited.copy()
        if point.islower():
            new_visited[point] += 1

        _can_visit_again = (can_visit_cave_again(new_visited)
            if part == 'B' else False)

        if point == 'end':
            cave_paths.append(_path)
            return

        for next_point in connections[point]:
            if next_point == 'start':
                continue
            elif next_point not in visited or _can_visit_again:
                _create_path(_path, new_visited, next_point)

    _create_path()
    return cave_paths

# solve A
all_paths = create_path()
print(f'Answer A: {len(all_paths)}')

# solve B
all_paths_b = create_path('B')
print(f'Answer B: {len(all_paths_b)}')

print()
t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
