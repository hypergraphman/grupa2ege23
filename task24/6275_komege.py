with open('24_6275.txt') as f:
    s = f.readline()

check = set('0123456789ABCDEF')
i = 0
j = 16
mn = len(s)
while j < len(s) or len(set(s[i:j]) & check) == 16:
    if len(set(s[i:j]) & check) < 16:
        j += 1
    else:
        mn = min(len(s[i:j]), mn)
        i += 1
print(mn)