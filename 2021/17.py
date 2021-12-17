
from time import perf_counter

t1_start = perf_counter()

# input - test
# MIN_X = 20; MAX_X = 30
# MIN_Y = -10; MAX_Y = -5

#target area: x=81..129, y=-150..-108
MIN_X, MAX_X = (81, 129)
MIN_Y, MAX_Y = (-150, -108)

"""
The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.

Due to drag, the probe's x velocity changes by 1 toward the value 0; 
  that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.

Answer for A could be calculated as:
y_min = -150
-ymin * ((-ymin - 1) / 2) = 11175

the solution below is how ever iterativ
and takes a couple of minuts to run

"""

answer = 0
count_hits = 0
for v_x in range(200):
    # print('outer', v_x, answer, count_hits)
    for v_y in range(-200, 1000):
        hit_target = False
        x = 0
        y = 0
        current_max_y = 0
        _x = v_x
        _y = v_y
        for _ in range(1000):
            x += _x
            y += _y
            current_max_y = max(current_max_y, y)
            # gravity
            if _x > 0:
                _x -= 1
            if _x < 0:
                _x += 1
            _y -= 1

            # did we hit target?
            if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y:
                hit_target = True
        if hit_target:
            count_hits += 1
            if current_max_y > answer:
                answer = current_max_y
                # print(v_x, v_y, answer, count_hits)

print()
print('answer A:', answer)
print('answer B:', count_hits)

print()

t1_stop = perf_counter()
print(f'Elapsed time during the whole program in seconds: {t1_stop-t1_start}')
