def f(line):
    while '>1' in line or '>2' in line or '>0' in line:
        if '>1' in line:
            line = line.replace('>1', '111>')
        if '>2' in line:
            line = line.replace('>2', '1>')
        if '>0' in line:
            line = line.replace('>0', '020>')
    return line[:-1]


for n in range(100, 200 + 1):
    for k in range(100, 200 + 1):
        for m in range(100, 200 + 1):
            s = '>' + k * '1' + m * '2' + n * '0'
            ans = sum(map(int, f(s)))
            if ans == 1190:
                print(n)