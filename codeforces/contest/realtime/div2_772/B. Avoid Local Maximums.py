import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split())) + [-1]

    cnt = 0
    for i in range(1, n - 1):
        if data[i - 1] < data[i] and data[i] > data[i + 1]:
            data[i + 1] = max(data[i], data[i + 2])
            cnt += 1

    print(cnt)
    print(*data[:-1])