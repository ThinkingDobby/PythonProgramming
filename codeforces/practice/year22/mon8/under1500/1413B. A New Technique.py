import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    rows = [list(map(int, input().split())) for _ in range(n)]
    cols = [list(map(int, input().split())) for _ in range(m)]

    chk = -1
    for i in range(m):
        if rows[0][0] in cols[i]:
            chk = i
            break

    rows.sort(key=lambda x: cols[chk].index(x[0]))
    for i in range(n):
        print(*rows[i])