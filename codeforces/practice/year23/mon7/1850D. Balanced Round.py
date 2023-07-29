import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = sorted(map(int, input().split()))

    memo = []
    for i in range(1, n):
        if data[i] - data[i - 1] > k:
            memo.append(i)

    if len(memo) == 0:
        print(0)
    else:
        mv = math.inf
        for i in range(1, len(memo)):
            mv = min(mv, memo[i - 1] + n - memo[i])
        ans = min(mv, n - memo[0], memo[-1])

        print(ans)
