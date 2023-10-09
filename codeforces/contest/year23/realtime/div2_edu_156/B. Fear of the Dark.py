import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    px, py = map(int, input().split())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())

    chk = [math.sqrt((ax - bx) ** 2 + (ay - by) ** 2) / 2]
    memo = [-1, -1]

    if (px - ax) ** 2 + (py - ay) ** 2 < (px - bx) ** 2 + (py - by) ** 2:
        chk.append(math.sqrt((px - ax) ** 2 + (py - ay) ** 2))
        memo[0] = 0
    elif (px - ax) ** 2 + (py - ay) ** 2 > (px - bx) ** 2 + (py - by) ** 2:
        chk.append(math.sqrt((px - bx) ** 2 + (py - by) ** 2))
        memo[0] = 1
    else:
        chk.append(math.sqrt((px - ax) ** 2 + (py - ay) ** 2))
        memo[0] = 2

    if ax ** 2 + ay ** 2 < bx ** 2 + by ** 2:
        chk.append(math.sqrt(ax ** 2 + ay ** 2))
        memo[1] = 0
    elif ax ** 2 + ay ** 2 > bx ** 2 + by ** 2:
        chk.append(math.sqrt(bx ** 2 + by ** 2))
        memo[1] = 1
    else:
        chk.append(math.sqrt(ax ** 2 + ay ** 2))
        memo[1] = 2

    if set(memo) == {0, 1}:
        print(max(chk))
    else:
        print(max(chk[1:]))
