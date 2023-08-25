import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    check = [data[i] % 2 for i in range(n)]

    evens = sorted([i for i in data if i % 2 == 0])
    odds = sorted([i for i in data if i % 2 == 1])

    sdata = [0] * n
    ei = 0
    oi = 0

    for i in range(n):
        if not check[i]:
            sdata[i] = evens[ei]
            ei += 1
        else:
            sdata[i] = odds[oi]
            oi += 1

    print("YES" if sdata == sorted(data) else "NO")