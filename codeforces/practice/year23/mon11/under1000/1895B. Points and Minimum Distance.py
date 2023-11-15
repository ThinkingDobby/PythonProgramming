import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    cnt = 0
    for i in range(1, n):
        cnt += data[i] - data[i - 1]
        cnt += data[-i] - data[-(i + 1)]

    print(cnt)
    for i in range(n):
        print(data[i], data[-(i + 1)])
