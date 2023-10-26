import collections
import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

memo = collections.defaultdict(list)
for i in range(n):
    heapq.heappush(memo[a[i]], -b[i])

cnt = 0
chk = []
for i in memo:
    if len(memo[i]) > 1:
        heapq.heappop(memo[i])
        chk += memo[i]

print(sum(sorted(map(lambda x: -x, chk))[:k - len(set(a))]))