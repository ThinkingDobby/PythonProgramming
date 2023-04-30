import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    chk1 = (x1 == 1 or x1 == n) + (y1 == 1 or y1 == m)
    chk2 = (x2 == 1 or x2 == n) + (y2 == 1 or y2 == m)

    print(4 - max(chk1, chk2))
