import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

ans = True
for i in range(n):
    for j in range(n):
        if data[i][j] != 1:
            chk = False
            for k in range(n):
                for l in range(n):
                    if data[i][k] + data[l][j] == data[i][j]:
                        chk = True
                        break
            if not chk:
                ans = False
                break

print("YES" if ans else "NO")