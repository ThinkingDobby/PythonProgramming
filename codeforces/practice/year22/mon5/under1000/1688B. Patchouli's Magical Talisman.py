# 미완성

import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk = [i for i in data if i % 2 == 0]
    if len(chk) != n:
        print(len(chk))
    else:
        memo = [math.inf for _ in range(n)]
        for i in range(n):
            cnt = 0
            tmp = data[i]
            while tmp % 2 == 1:
                tmp //= 2
                cnt += 1
            memo[i] = cnt

        print(min(memo) + len(chk) - 1)

