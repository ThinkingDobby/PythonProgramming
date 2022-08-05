import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = collections.defaultdict(int)
    ans = 0
    for i in range(n - 1, -1, -1):
        memo[data[i]] += 1
        if memo[data[i]] == 2:
            ans = i + 1
            break

    print(ans)


