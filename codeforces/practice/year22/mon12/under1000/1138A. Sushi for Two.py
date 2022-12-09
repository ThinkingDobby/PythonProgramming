import sys

input = sys.stdin.readline

fc = 0
sc = 0

n = int(input())
data = list(map(int, input().split())) + [3]
cnt = 1
prev = 0

for i in range(1, n + 1):
    if data[i - 1] != data[i]:
        if data[i - 1] == 1:
            fc = max(fc, min(cnt, prev))
            prev = cnt
        else:
            sc = max(sc, min(cnt, prev))
            prev = cnt
        cnt = 1
    else:
        cnt += 1

print(max(fc, sc) * 2)