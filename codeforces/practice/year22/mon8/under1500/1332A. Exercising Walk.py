import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())

    ans = True

    if x1 == x2 and a + b != 0:
        ans = False
    if y1 == y2 and c + d != 0:
        ans = False

    th = b - a
    tv = d - c

    if x2 - x1 > 1:
        if a > b:
            th = -(a - b)
        else:
            th = b - a
    if y2 - y1 > 1:
        if c > d:
            tv = -(c - d)
        else:
            tv = d - c

    if th > 0:
        if th > x2 - x:
            ans = False
    else:
        if th < x1 - x:
            ans = False
    if tv > 0:
        if tv > y2 - y:
            ans = False
    else:
        if tv < y1 - y:
            ans = False

    print("YES" if ans else "NO")
