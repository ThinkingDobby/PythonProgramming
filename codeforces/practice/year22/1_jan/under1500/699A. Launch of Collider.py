import math

n = int(input())
dir = list(input())
x = list(map(int, input().split()))

ans = math.inf
for i in range(1, n):
    if dir[i - 1] == 'R' and dir[i] == 'L':
        ans = min(ans, (x[i] - x[i - 1]) // 2)

if ans == math.inf:
    print(-1)
else:
    print(ans)
