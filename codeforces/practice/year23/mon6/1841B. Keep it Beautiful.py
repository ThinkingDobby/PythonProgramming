# WA

import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    mv = math.inf
    prev = -1

    check = False
    cmv = -1
    for i in data:
        if i < prev:
            if not check and i <= mv:
                check = True
                cmv = mv
            else:
                print(0, end='')
                continue
        else:
            if check and i > cmv:
                print(0, end='')
                continue
            mv = min(mv, i)

        prev = i
        print(1, end='')

    print()