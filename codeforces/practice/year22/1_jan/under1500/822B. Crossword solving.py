import math

n, m = map(int, input().split())
s = list(input())
t = list(input())

idx = -1
mv = math.inf

for i in range(m - n + 1):
    cnt = 0
    for j in range(n):
        if s[j] != t[i + j]:
            cnt += 1
    if cnt < mv:
        idx = i
        mv = cnt

print(mv)
for i in range(n):
    if s[i] != t[idx + i]:
        print(i + 1, end=' ')