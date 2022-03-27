import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    s = 0

    if 0 in data:
        print(n - data[::-1].index(0) - data.index(0) + 1)
    else:
        print(0)