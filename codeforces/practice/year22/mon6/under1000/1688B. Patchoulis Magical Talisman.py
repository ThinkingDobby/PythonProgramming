import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = [i for i in data if i % 2 == 1]
    if len(tmp) != 0:
        print(n - len(tmp))
    else:
        mv = math.inf
        for i in data:
            if i % 2 == 0:
                cnt = 0
                while i % 2 == 0:
                    i /= 2
                    cnt += 1
                mv = min(cnt, mv)
        print(mv + n - len(tmp) - 1)