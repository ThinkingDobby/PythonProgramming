import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    mv = math.inf
    for i in range(1, n):
        mv = min(mv, max(data[i - 1], data[i]))

    print(mv - 1)