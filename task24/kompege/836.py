line = open('24.txt').readline()
k = 0
for i in range(4, len(line)):
    s1, s2, s4, s5 = line[i - 4], line[i - 3], line[i - 1], line[i]
    if s1 == s5 and s2 == s4:
        k += 1
print(k)