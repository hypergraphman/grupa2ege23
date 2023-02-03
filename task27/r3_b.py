f = open('27_B.txt')
n = int(f.readline())
k = 999
tail_sum = [0] + [None] * (k - 1)
tail_len = [0] * k
mx = 0
mx_len = 0
total_sum = 0
for i in range(1, n + 1):
    x = int(f.readline())
    total_sum += x
    r = total_sum % k
    if tail_sum[r]:
        cur_sum = total_sum - tail_sum[r]
        cur_len = i - tail_len[r]
        if cur_sum > mx:
            mx = cur_sum
            mx_len = cur_len
        elif cur_sum == mx and mx_len > cur_len:
            mx_len = cur_len
    else:
        tail_sum[r] = total_sum
        tail_len[r] = i
print(mx_len)

# 844158