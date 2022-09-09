import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    mv = -math.inf
    for i in range(n):
        mv = max(data[n - 1 - i] - data[-i], mv)
    print(max(data[-1] - min(data), max(data) - data[0], mv))
