from math import inf


def check(n):
    sum_odd = sum(map(int, str(n)[-2::-2]))
    sum_even = sum(map(int, str(n)[::-2]))
    try:
        return sum_odd % sum_even == 0
    except:
        return False


data = tuple(map(int, open('17-343.txt').readlines()))
#print(data)
k = 0
min_sum = inf
for i in range(2, len(data)):
    p1, p2, p3 = data[i - 2], data[i - 1], data[i]
    if check(p1) and check(p2) and check(p3):
        k += 1
        min_sum = min(p1 + p2 + p3, min_sum)
print(k, min_sum)
# 124 4103