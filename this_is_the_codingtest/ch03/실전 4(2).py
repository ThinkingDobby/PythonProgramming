import sys

input = sys.stdin.readline

n, k = map(int, input().split())

now = n
cnt = 0
while now > 1:
    if now % k == 0:
        now //= k
        cnt += 1
    else:
        now -= 1
        cnt += 1

print(cnt)