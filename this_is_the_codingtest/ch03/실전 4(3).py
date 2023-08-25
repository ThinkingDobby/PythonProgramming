import sys

input = sys.stdin.readline

n, k = map(int, input().split())

now = n

cnt = 0
while now > 1:
    cnt += now - (now // k) * k + 1
    now //= k

print(cnt)