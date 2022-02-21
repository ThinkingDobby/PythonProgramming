import sys
inp = sys.stdin.readline

for _ in range(int(inp())):
    n = int(inp())
    enemy = list(map(int, input()))
    my = list(map(int, input()))

    cnt = 0
    for i in range(n):
        if my[i] == 1:
            if enemy[i] == 0:
                cnt += 1
            else:
                if i > 0:
                    if enemy[i - 1] == 1:
                        cnt += 1
                        enemy[i - 1] = 2
                        continue
                if i < n - 1:
                    if enemy[i + 1] == 1:
                        cnt += 1
                        enemy[i + 1] = 2

    print(cnt)