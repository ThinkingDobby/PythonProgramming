import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [input().rstrip() for _ in range(n)]
    name = "vika"

    now = 0
    ans = False
    for j in range(m):
        for i in range(n):
            if data[i][j] == name[now]:
                now += 1
                if now > 3:
                    ans = True
                break

        if now > 3:
            break

    print("YES" if ans else "NO")

