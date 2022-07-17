import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if data[0] == 0:
        idx = 1
        for i in range(1, n):
            if data[i] != 0:
                idx = i
                break
            if i == n - 1 and data[i] == 0:
                idx = -1
        print(sum(data[idx:-1]) + data[idx:-1].count(0))
    else:
        print(sum(data[:-1]) + data[:-1].count(0))