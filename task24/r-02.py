with open('24.txt') as f:
    line = f.readline()

cur_len = 0
max_len = 0
for c in line:
    if c in 'ABC':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
print(max_len)
