import sys

input = sys.stdin.readline

n, d = map(int, input().split())

data = [list(map(int, input().rstrip())) for _ in range(d)]

memo = [all(i) for i in data]

cnt = 0
mv = 0
for i in memo:
    if i == 0:
        cnt += 1
        mv = max(mv, cnt)
    else:
        cnt = 0

print(mv)