import sys

input = sys.stdin.readline


def dfs(x, y, z):
    global chk
    if chk:
        return

    if x * 3 + y * 5 + z * 7 == n:
        chk = True
        print(x, y, z)
        return
    elif x * 3 + y * 5 + z * 7 > n:
        return
    dfs(x + 1, y, z)
    dfs(x, y + 1, z)
    dfs(x, y, z + 1)

    return


for _ in range(int(input())):
    n = int(input())

    chk = False
    dfs(0, 0, 0)
    if not chk:
        print(-1)

