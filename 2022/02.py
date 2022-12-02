
input_file = 'input/02.txt'
matches = [v.strip().split() for v in open(input_file, 'r').readlines()]

# --- RULES --- #
points = {'X': 1, 'Y': 2, 'Z': 3}

wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
even = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loss = {'A': 'Z', 'B': 'X', 'C': 'Y'}

# A
score = 0
for g in matches:
    score += points[g[1]]
    if (g[0], g[1]) in wins.items():
        score += 6
    elif (g[0], g[1]) in even.items():
        score += 3
print(f'Part 1: {score}')

# B: X, lose, Y = even, Z = win
score = 0
for g in matches:
    if g[1] == 'Z': # win
        score += 6 + points[wins[g[0]]]
    elif g[1] == 'Y': # even
        score += 3 + points[even[g[0]]]
    else: # lose
        score += points[loss[g[0]]]

print(f'Part 2: {score}')
