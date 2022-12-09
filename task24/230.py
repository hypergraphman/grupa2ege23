from re import fullmatch


lines = open('24-230.txt').readline().split('ZZ')

mx = 0
for line in lines:
    if fullmatch(r'8\d\d\d54\d\d\d22', line):
        mx = max(int(line), mx)

p = 1
while mx > 0:
    if mx % 10 % 2:
        p *= mx % 10
    mx //= 10
print(p)
