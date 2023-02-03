# максимальная подпоследовательность в которой кол-во чисел делящихся на 11
# кратно 7
f = open('test.txt')
# k_11 = 0
a = [int(x) for x in f]
# print(sum(a)) # 544982
# ms = 0
# for i in range(len(a)):
#     s = 0
#     k_11 = 0
#     for j in range(i, len(a)):
#         s += a[j]
#         if a[j] % 11 == 0:
#             k_11 += 1
#         if k_11 % 7 == 0:
#             ms = max(ms, s)
# print(ms)
# 541908

print(len(list(filter(lambda x: x % 11 == 0, a))) % 7)
s = 0
k = 0
for el in a:
    s += el
    if el % 11 == 0:
        k += 1
    if k == 4:
        print(s)
        break
print(544982 - s)

s = 0
k = 0
for el in a:
    s += el
    if el % 11 == 0:
        k += 1
    if k == 78:
        print(s - el)
        break
# ms = 0
# s = 0
# k_11 = 0
# min_tails = [0] + [10**20] * 7
# for el in f:
#     el = int(el)
#     s += el
#     if el % 11 == 0:
#         k_11 += 1
#     ms = max(ms, s - min_tails[k_11 % 7])
#     min_tails[k_11 % 7] = min(min_tails[k_11 % 7], s)
# print(ms)
# 522618