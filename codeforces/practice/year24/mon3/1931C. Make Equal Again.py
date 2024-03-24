import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    fcnt = 1
    scnt = 1
    for i in range(1, n):
        if data[i] == data[0]:
            fcnt += 1
        else:
            break
    for i in range(1, n):
        if data[-(i + 1)] == data[-1]:
            scnt += 1
        else:
            break

    ans = -1
    if data[0] == data[-1]:
        ans = min(n, fcnt + scnt)
    else:
        ans = max(fcnt, scnt)

    print(n - ans)
