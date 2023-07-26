import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    mv = math.inf
    for i in range(1, n):
        mv = min(mv, data[i] - data[i - 1])

    ans = max(0, mv // 2 + 1)
    print(ans)