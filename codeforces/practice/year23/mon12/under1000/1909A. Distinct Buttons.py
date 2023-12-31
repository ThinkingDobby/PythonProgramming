import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    chk = [False] * 4

    for x, y in data:
        if x > 0:
            chk[0] = True
        if x < 0:
            chk[1] = True
        if y > 0:
            chk[2] = True
        if y < 0:
            chk[3] = True

    print("YES" if chk.count(True) <= 3 else "NO")