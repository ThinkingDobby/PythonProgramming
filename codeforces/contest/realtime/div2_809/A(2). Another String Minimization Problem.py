import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(lambda x: int(x) - 1 if int(x) - 1 < (m + 1) // 2 else m - int(x), input().split()))
    data_cnt = dict(collections.Counter(data))

    memo = ['B' for _ in range(m)]
    for i in data_cnt:
        if data_cnt[i] > 1:
            memo[i] = 'A'
            memo[m - 1 - i] = 'A'
        elif data_cnt[i] == 1:
            memo[i] = 'A'

    for i in memo:
        print(i, end='')
    print()
