import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: -x[1])

cnt = n
ans = 0
for a, b in data:
    tmp = min(cnt, a)
    ans += tmp * b

    cnt -= tmp

    if cnt <= 0:
        break

print(ans)
