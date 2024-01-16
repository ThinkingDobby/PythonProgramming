import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    min_v = -1
    max_v = math.inf
    not_v = set()

    for _ in range(n):
        typ, x = map(int, input().split())

        if typ == 1:
            min_v = max(min_v, x)
        elif typ == 2:
            max_v = min(max_v, x)
        elif typ == 3:
            not_v.add(x)

    if min_v > max_v:
        print(0)
    else:
        print(max_v - min_v + 1 - len([i for i in not_v if min_v <= i <= max_v]))