# максимальную подпоследовательность сумма кратная 100
f = open('test.txt')
k = 100
# ms = 0
# for i in range(len(a)):
#     s = 0
#     for j in range(i, len(a)):
#         s += a[j]
#         if s % k == 0:
#             ms = max(ms, s)
# print(ms)
# 533800

min_tail = [0] + [10**20] * (k - 1)
s = 0
ms = 0
for el in f:
    s += int(el)
    min_tail[s % k] = min(s, min_tail[s % k])
    ms = max(ms, s - min_tail[s % k])
# print(min_tail)

# s = 0
# ms = 0
# for el in a:
#     s += el
#     ms = max(ms, s - min_tail[s % k])
print(ms)