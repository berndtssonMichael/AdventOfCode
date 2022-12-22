

coords = [tuple(int(i) for i in s.split(',')) for s in open('input/18.txt')]

def get_neighbours(x, y, z):
    return (
        (x - 1, y, z), (x + 1, y, z),
        (x, y - 1, z), (x, y + 1, z),
        (x, y, z - 1), (x, y, z + 1)
    )

def solve_a(coords):
    cnt = 0
    for x, y, z in coords:

        for nx, ny, nz in get_neighbours(x, y, z):
            cnt += (nx, ny, nz) in coords

    return len(coords) * 6 - cnt

def solve_b(coords):
    # outer_boundaries
    min_pos = min(min(i) for i in coords) - 1
    max_pos = max(max(i) for i in coords) + 2

    cnt = 0
    outside_coords = [(min_pos, min_pos, min_pos)]
    visited = set()
    while outside_coords:
        x, y, z = outside_coords.pop()
        if (x, y, z) not in visited:
            visited.add((x, y, z))
            for ox, oy, oz in get_neighbours(x, y, z):
                if all(min_pos <= i <= max_pos for i in (ox, oy, oz)):
                    if (ox, oy, oz) in coords:
                        cnt += 1
                    else:
                        outside_coords.append((ox, oy, oz))
    return cnt


print(f'answer A: {solve_a(coords)}')
print(f'answer B: {solve_b(coords)}')
