import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    cnt = 1
    tot = 0
    base = data[-1]

    i = n - 2
    while cnt < n and i >= 0:
        if data[i] == base:
            cnt += 1
            i -= 1
        else:
            tot += 1
            i -= cnt
            cnt *= 2

    print(tot)