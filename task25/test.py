from time import time

st = time()
for i in range(11*10**6):
    i += 1
    for j in range(4000):
        j += 1
print(time() - st)