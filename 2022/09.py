# moves = [v.strip().split() for v in open('input/test.txt', 'r').readlines()]
moves = [v.strip().split() for v in open('input/09.txt', 'r').readlines()]

class Knot():
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def pos(self):
        return (self.x, self.y)



def solve(moves, no_of_knots):

    visited = set()

    # create a rope with correct no of knots
    rope = [Knot() for i in range(no_of_knots)]

    head = rope[0]
    tail = rope[-1]
    visited.add(tail.pos())


    for m in moves:
        direction, steps = m[0], int(m[1])

        for step in range(1, steps + 1):
            # First bove head
            if direction == "U":
                head.x -= 1
            elif direction == "D":
                head.x += 1
            elif direction == "L":
                head.y -= 1
            elif direction == "R":
                head.y += 1

            # then change all tails
            for i in range(1, len(rope)):
                _head = rope[i - 1]
                _tail = rope[i]

                x_diff = _head.x - _tail.x
                y_diff = _head.y - _tail.y
                # Move tail to keep up with head
                # head_tail are touching, do nothing
                if abs(x_diff) <= 1 and abs(y_diff) <= 1:
                    continue
                # moving along y
                elif (x_diff) == 0:
                    _tail.y += (y_diff) // abs(y_diff)
                # moving along x
                elif (y_diff) == 0:
                    _tail.x += (x_diff) // abs(x_diff)
                # moving diagonally
                else:
                    _tail.x += (x_diff) // abs(x_diff)
                    _tail.y += (y_diff) // abs(y_diff)
                # Add current tail position to set of visited positions
                visited.add(tail.pos())

    return len(visited)

print('A:', solve(moves, 2))
print('B:', solve(moves, 10))
