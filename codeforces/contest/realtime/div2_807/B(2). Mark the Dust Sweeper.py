import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    start = n - 1
    for i in range(n - 1):
        if data[i] != 0:
            start = i
            break

    cnt = 0
    for i in range(start, n - 1):
        if data[i] == 0:
            cnt += 1

    print(cnt + sum(data[:-1]))