# кол-во подпоследовательностей сумма которых кратна 67
f = open('test.txt')
k = 67
# a = [int(x) for x in f]
# c = 0
# for i in range(len(a)):
#     s = 0
#     for j in range(i, len(a)):
#         s += a[j]
#         if s % k == 0:
#             c += 1
# print(c)
# 7508

count_min_tail = [0] * k
s = 0
count = 0
for el in f:
    s += int(el)
    if s % k == 0:
        count += 1
    count += count_min_tail[s % k]

    count_min_tail[s % k] += 1
print(count)