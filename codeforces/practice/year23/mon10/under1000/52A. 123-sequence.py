import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

cntr = collections.Counter(data)
ans = sum(sorted(cntr.values())[:-1])

print(ans)