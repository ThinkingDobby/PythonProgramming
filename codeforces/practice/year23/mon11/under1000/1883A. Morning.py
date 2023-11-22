import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().rstrip()))
    for i in range(4):
        if data[i] == 0:
            data[i] = 10

    cnt = data[0] - 1 + 4
    now = data[0]
    for i in range(1, 4):
        cnt += abs(now - data[i])
        now = data[i]

    print(cnt)