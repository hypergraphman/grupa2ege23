with open('24-235.txt') as f:
    line = f.readline()

cur_len = 1
max_len = 1
max_s = line[0]
for i in range(1, len(line)):
    c1, c2 = line[i - 1], line[i]
    if c1 != c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            max_s = line[i - max_len + 1:i + 1]
        elif cur_len == max_len:
            max_s = line[i - max_len + 1:i + 1]
    else:
        cur_len = 1
print(max_len, max_s)

stat = dict()
for c in max_s:
    if c in stat:
        stat[c] += 1
    else:
        stat[c] = 1
print(stat)
# mx_k, mx_v = '', 0
# for k, v in stat.items():
#     if v > mx_v:
#         mx_k, mx_v = k, v
# print(mx_k, mx_v)
print(max(stat.items(), key=lambda kv: kv[1]))
print(0)