import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(3)]

    tmp = 0

    for i in range(3):
        for j in range(n):
            if x | data[i][j] != x:
                break
            tmp |= data[i][j]

    print("Yes" if tmp == x else "No")
