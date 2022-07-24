import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    half = (m + 1) // 2
    data = list(map(lambda x: int(x) - 1, input().split()))
    cdata = dict(collections.Counter([i if i < half else m - i - 1 for i in data]))

    memo = ['B' for _ in range(m)]
    for i in cdata:
        if cdata[i] >= 2:
            memo[i] = 'A'
            memo[-(i + 1)] = 'A'
        else:
            memo[i] = 'A'

    for i in memo:
        print(i, end='')
    print()