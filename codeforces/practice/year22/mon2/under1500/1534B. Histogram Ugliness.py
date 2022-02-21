import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split())) + [0]

    cnt = data[-2]
    for i in range(1, n + 1):
        cnt += abs(data[i] - data[i - 1])
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            cnt -= data[i] - max(data[i - 1], data[i + 1])

    print(cnt)
