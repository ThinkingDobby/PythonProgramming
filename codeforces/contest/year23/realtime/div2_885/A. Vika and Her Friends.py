import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    x, y = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(k)]

    ans = True
    for i in range(k):
        tmp = abs(data[i][0] - x) + abs(data[i][1] - y)
        if tmp % 2 == 0:
            ans = False
            break

    print("YES" if ans else "NO")