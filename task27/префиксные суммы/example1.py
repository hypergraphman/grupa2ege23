from random import randint
from time import time


a = [randint(10, 99) for _ in range(1_000_000)]
pre_a = [0]
for el in a:
    pre_a.append(pre_a[-1] + el)

start = time()
print(sum(a[500:500_000]))
print(time() - start)

start = time()
print(pre_a[500_000] - pre_a[500])
print(time() - start)