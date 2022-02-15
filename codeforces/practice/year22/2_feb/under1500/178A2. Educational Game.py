import math

n = int(input())
data = list(map(int, input().split()))

for k in range(n - 1):
    cnt = 0
    for i in range(k + 1):
        tmp = i
        while 2**(int(math.log2(n - 1 - tmp))) + tmp <= k:
            cnt += data[i]
            tmp = 2 ** (int(math.log2(n - 1 - tmp))) + tmp
        cnt += data[i]
    print(cnt)
