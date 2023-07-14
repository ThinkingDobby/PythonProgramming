# WA

import sys

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)] + [-1]

prev = 2
cnt = 0
ans = True
for i in range(1, n + 1):
    if data[i - 1] != data[i]:
        if cnt % 2 == 0 and data[i] == prev:
            ans = False
            break
        elif cnt % 2 == 1 and data[i] != prev:
            ans = False
            break
        else:
            cnt = 0
            prev = data[i - 1]
    else:
        cnt += 1

print("YES" if ans else "NO")