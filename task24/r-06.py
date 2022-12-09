line = open('k8.txt').readline()

cur_len = 1
max_len = 1
find_lines = [line[0]]
for i in range(1, len(line)):
    c1, c2 = line[i - 1], line[i]
    if c1 == c2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            find_lines = [c2]
        elif cur_len == max_len:
            find_lines.append(c2)
    else:
        cur_len = 1

print(*find_lines)
