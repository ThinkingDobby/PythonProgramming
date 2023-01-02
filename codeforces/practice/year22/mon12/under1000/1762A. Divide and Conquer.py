import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if sum(data) % 2 == 0:
        print("0")
    else:
        mv = math.inf
        for i in data:
            tmp = i % 2
            now = i
            cnt = 0
            while now % 2 == tmp:
                cnt += 1
                now //= 2
            mv = min(mv, cnt)

        print(mv)
