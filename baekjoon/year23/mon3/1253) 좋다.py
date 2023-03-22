import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

chk = collections.defaultdict(int)
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        chk[data[i] + data[j]] = 1
        if (data[i] == 0) ^ (data[j] == 0):
            cnt -= 1

for i in data:
    cnt += chk[i]

print(cnt if n > 2 else 0)