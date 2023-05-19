import sys

input = sys.stdin.readline

n, b, d = map(int, input().split())
data = list(map(int, input().split()))

memo = [i for i in data if i <= b]

cnt = 0
tot = 0
for i in memo:
    tot += i
    if tot > d:
        cnt += 1
        tot = 0

print(cnt)
