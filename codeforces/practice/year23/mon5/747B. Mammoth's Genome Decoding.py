import collections
import sys

input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())

memo = dict(collections.Counter(data))
tmp = ['A', 'C', 'G', 'T']

for i in tmp:
    if i not in memo:
        memo[i] = 0

if n % 4 != 0 or max([memo[i] for i in memo.keys() if i != '?']) > n // 4:
    print("===")
else:
    now = 0

    for i in range(n):
        if data[i] == '?':
            while memo[tmp[now]] + 1 > n // 4:
                now += 1
            else:
                memo[tmp[now]] += 1
                print(tmp[now], end='')
        else:
            print(data[i], end='')
