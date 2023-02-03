l = '0' + '1112211221111221221221' + '21' * 17 + '22' + '0'
print(l.count('1'), l.count('2'), l)
while '00' not in l:
    l = l.replace('011', '20', 1)
    l = l.replace('022', '10', 1)
    l = l.replace('01', '220', 1)
    l = l.replace('02', '110', 1)
    print(l)
print(l.count('1'), l.count('2'), l)