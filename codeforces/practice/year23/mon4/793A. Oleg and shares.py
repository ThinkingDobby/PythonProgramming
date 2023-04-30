import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

memo = min(data)

ans = True
cnt = 0
for i in range(n):
    if (data[i] - memo) % k != 0:
        ans = False
    else:
        cnt += (data[i] - memo) // k

print(cnt if ans else -1)