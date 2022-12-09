line = open('k7.txt').readline()

count = 0
for i in range(2, len(line)):
    c1, c2, c3 = line[i - 2], line[i - 1], line[i]
    if (c1 in 'BCD' and c2 in 'BDE' and c2 != c1 and
       c3 in 'BCE' and c3 != c2):
        count += 1
print(count)
