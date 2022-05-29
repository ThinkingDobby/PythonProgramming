import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

idx = -1
for i in range(0, m - 1):
    if data[i] <= k and data[i] != 0:
        idx = i

for i in range(m - 1, n):
    if data[i] <= k and data[i] != 0:
        if idx != -1:
            if m - 1 - idx > i - (m - 1):
                idx = i
                break
        else:
            idx = i
            break

print(abs((m - 1) - idx) * 10)
