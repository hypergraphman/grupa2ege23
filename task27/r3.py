f = open('27_A.txt')
n = int(f.readline())
a = list(map(int, f.readlines()))
print(a)
mx = -1
mx_len = -1
for i in range(n):
    for j in range(i + 1, n + 1):
        t = a[i:j]
        st = sum(t)
        if st % 43 == 0 and st > mx:
            mx = st
            mx_len = len(t)
            print(mx, mx_len)
        elif st % 43 == 0 and st == mx:
            if len(t) < mx_len:
                mx_len = len(t)
                print(mx, mx_len)
print(mx_len)
# 185
