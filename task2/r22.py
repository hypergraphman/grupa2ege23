# 1
print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or y) and not (y == z) and not w
                if f:
                    print(x, y, z, w, int(f))

# 2
from itertools import product

print('x y z w f')
for x, y, z, w in product((0, 1), repeat=4):
    f = (x or y) and not (y == z) and not w
    if f:
        print(x, y, z, w, int(f))
