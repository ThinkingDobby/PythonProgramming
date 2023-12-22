import sys

input = sys.stdin.readline

n, d = map(int, input().split())
data = sorted(map(int, input().split()), reverse=True)

cnt = n
ans = 0
for i in range(n):
    tmp = (d + data[i]) // data[i]
    if cnt < tmp:
        break

    cnt -= tmp
    ans += 1

print(ans)