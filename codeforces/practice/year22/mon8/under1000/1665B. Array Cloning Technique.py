import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    memo = collections.defaultdict(int)
    for i in data:
        memo[str(i)] += 1
    mc = max(memo.values())

    cnt = 0
    tmp = mc
    while tmp < n:
        tmp *= 2
        cnt += 1

    print(cnt + n - mc)
