import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(input().rstrip())

    memo = collections.defaultdict(int)
    for i in data:
        memo[i] += 1

    ans = ''
    for i in range(97, 123):
        ans += chr(i) * max(0, k - memo[chr(i)])

    print(memo)
    print(ans)