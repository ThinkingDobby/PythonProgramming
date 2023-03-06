import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    s = sum(data)
    ans = -math.inf
    for i in range(1, n):
        ans = max(s - (data[i - 1] + data[i]) * 2, ans)

    print(ans)
