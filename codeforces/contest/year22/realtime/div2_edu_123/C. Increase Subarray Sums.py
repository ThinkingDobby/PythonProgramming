import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    data = list(map(int, input().split()))
    memo = [0] * (n + 1)
    memo[1] = data[0]
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + data[i - 1]

    cnts = {i:-math.inf for i in range(1, n + 1)}
    for i in range(n):
        for j in range(i + 1, n + 1):
            cnts[j - i] = max(cnts[j - i], memo[j] - memo[i])

    scnts = sorted(list(cnts.items()), key=lambda x: (-x[1], -x[0]))

    k = 0
    now = 0
    mv = 0
    while True:
        if scnts[now][0] >= k:
            tmp = k * x + scnts[now][1]
            mv = max(mv, tmp)
            print(mv, end=' ')
            k += 1
            if k == n + 1:
                break
        else:
            now += 1
            if now == n + 1:
                break
    print()