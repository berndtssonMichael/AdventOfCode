import string
import networkx as nx

# parse grid
grid = [list(line.strip()) for line in open('input/12.txt', 'r').readlines()]

# init values
width = len(grid[0])
height = len(grid)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
start_x, start_y = None, None
end_x, end_y = None, None

# find start end end position and reset values on these
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            start_x, start_y = x, y
            grid[y][x] = 'a'
        elif grid[y][x] == 'E':
            end_x, end_y = x, y
            grid[y][x] = 'z'

# Create an empty graph structure (a “null graph”) with no nodes and no edges.
G = nx.DiGraph()
for y in range(height):
    for x in range(width):
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y

            # check that were not outside the grid
            if 0 <= new_x < width and 0 <= new_y < height:
                curr_val = string.ascii_lowercase.index(grid[y][x])
                new_val = string.ascii_lowercase.index(grid[new_y][new_x])

                # if new value is one larger then current value add to Graf
                if new_val <= curr_val + 1:
                    G.add_edge((x, y), (new_x, new_y))

# use networkx shortest_path_length to get answer for A
print(f'A: {nx.shortest_path_length(G, (start_x, start_y), (end_x, end_y))}')

path_len_b = width * height  # initial value, total grid
visit_all = width * height

# go throw grid to find all posible start points, i.e. 'a'
for y in range(height):
    for x in range(width):
        if grid[y][x] == 'a':
            try:
                path_len = nx.shortest_path_length(G, (x, y), (end_x, end_y))
                path_len_b = min(path_len_b, path_len)
            except:
                pass

print(f'B: {path_len_b}')
