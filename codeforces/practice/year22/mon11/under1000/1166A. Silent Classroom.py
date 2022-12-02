import collections
import math
import sys

input = sys.stdin.readline

data = collections.Counter(input().rstrip()[0] for _ in range(int(input())))
cnts = sorted(data.values())
cnt = 0

for i in cnts:
    cnt += math.comb((i + 1) // 2, 2) + math.comb(i // 2, 2)

print(cnt)