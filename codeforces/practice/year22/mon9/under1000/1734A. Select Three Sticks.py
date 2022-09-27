import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    mv = math.inf
    for i in range(1, n - 1):
        mv = min(mv, data[i] - data[i - 1] + data[i + 1] - data[i])

    print(mv)
