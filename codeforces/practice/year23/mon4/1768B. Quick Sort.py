import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    mv = math.inf
    tmp = math.inf
    for i in range(n - 1, - 1, - 1):
        mv = min(mv, data[i])
        if data[i] > mv:
            tmp = min(tmp, data[i])

    memo = (n - tmp + 1) if tmp != math.inf else 0
    ans = (memo + k - 1) // k
    print(ans)
