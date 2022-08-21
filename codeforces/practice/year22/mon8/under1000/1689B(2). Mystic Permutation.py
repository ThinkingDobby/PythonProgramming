import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    sdata = sorted(data)
    memo = [0] * n
    for i in range(1, n):
        if sdata[i - 1] == data[i - 1]:
            sdata[i - 1], sdata[i] = sdata[i], sdata[i - 1]

    if sdata[n - 1] == data[n - 1]:
        sdata[n - 2], sdata[n - 1] = sdata[n - 1], sdata[n - 2]

    print(*sdata)