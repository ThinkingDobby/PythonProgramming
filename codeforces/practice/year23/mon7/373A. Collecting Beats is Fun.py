import collections
import itertools
import sys

input = sys.stdin.readline

k = int(input())

data = [list(input().rstrip()) for _ in range(4)]
cntr = collections.Counter(itertools.chain(*data))

mv = -1
for i in cntr:
    mv = max(mv, cntr[i]) if i != '.' else mv

print("NO" if mv > 2 * k else "YES")