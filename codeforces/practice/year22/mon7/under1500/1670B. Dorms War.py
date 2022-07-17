# 미완성

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    tmp = set(input().split()[1:])

    cnt = 0
    mv = 0
    for i in range(n):
        if data[i] in tmp:
            mv = cnt
            cnt = 0
        cnt += 1

    print(mv)
