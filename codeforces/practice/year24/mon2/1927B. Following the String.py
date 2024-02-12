# TLE
import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = collections.defaultdict(set)
    for i in range(26):
        memo[0].add(chr(i + 97))

    ans = ''
    for i in data:
        tmp = memo[i].pop()
        memo[i + 1].add(tmp)

        ans += tmp

    print(ans)