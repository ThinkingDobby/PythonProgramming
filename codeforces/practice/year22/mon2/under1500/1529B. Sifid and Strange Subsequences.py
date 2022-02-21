import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))
    mv = math.inf
    cnt = 1

    for i in range(1, n):
        mv = min(mv, abs(data[i] - data[i - 1]))
        if mv < data[i]:
            break
        cnt += 1
    print(cnt)