with open('24.txt') as f:
    mx_len = 0
    mx_line = ''
    mx_char = ''
    for line in f.readlines():
        cur_len = 1
        for i in range(1, len(line)):
            if line[i - 1] == line[i]:
                cur_len += 1
                if cur_len == 5:
                    mx_line = line
                    mx_char = line[i]
                    print(mx_char, mx_line.count(mx_char))
            else:
                cur_len = 1