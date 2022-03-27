import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    memo = [0] * 30
    n, x = map(int, input().split())
    data = list(map(int, input().split()))

    mv = math.inf
    idx = -1
    for i in range(n):
        cnt = 1
        tmp = data[i]
        while tmp % x == 0:
            cnt += 1
            tmp //= x

        if mv > cnt:
            mv = cnt
            idx = i

    print(sum(data) * mv + sum(data[:idx]))