from itertools import permutations


def alg(n):
    m = []
    for d1, d2 in permutations(str(n), r=2):
        num = int(d1 + d2)
        if 10 <= num <= 99:
            m.append(num)
    return max(m) - min(m)


i = 100
while alg(i) != 40:
    i += 1
print(i)
