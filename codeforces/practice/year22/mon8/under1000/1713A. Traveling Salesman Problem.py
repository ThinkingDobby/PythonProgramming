import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    x_memo = [0]
    y_memo = [0]

    for _ in range(n):
        x, y = map(int, input().split())
        if x == 0:
            y_memo.append(y)
        else:
            x_memo.append(x)

    print((max(y_memo) - min(y_memo)) * 2 + (max(x_memo) - min(x_memo)) * 2)
