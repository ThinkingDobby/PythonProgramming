import sys

input = sys.stdin.readline

c, v0, v1, a, l = map(int, input().split())
tot = 0

now = 0
while True:
    now += 1
    tot += min(v1, v0)
    v0 += a
    if tot >= c:
        break
    tot -= l

print(now)