# 13123401234123401123412302342134
lines = open('24-232.txt').readline().split('0')[1:-1]
max_line = ''
for line in lines:
    if sum(map(int, line)) % 5 == 0 and len(line) > len(max_line):
        max_line = line
print(sum(map(int, max_line)))
