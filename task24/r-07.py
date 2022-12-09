with open('24.txt') as f:
    line = f.readline()

cur_len = 1
max_len = 1
for i in range(1, len(line)):
    c1, c2 = line[i - 1], line[i]
    if c1 != c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1
print(max_len)
