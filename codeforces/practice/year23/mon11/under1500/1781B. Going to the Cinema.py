import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split())) + [math.inf]

    cnt = data[0] != 0
    for i in range(n):
        if i >= data[i] and i + 1 < data[i + 1]:
            cnt += 1

    print(cnt)