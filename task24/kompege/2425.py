line = open('24.txt').readline()

cur_len = 0
max_len = 0
#    012
t = 'DBAC'
n = len(t)
for i in range(len(line)):
    c = line[i]
    if c == t[cur_len % n]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0
        if c == t[0]:
            cur_len = 1
print(max_len)
