import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    mv = math.inf
    if k == 4:
        even_cnt = len([i for i in data if i % 2 == 0])
        mv = min(mv, 2 - min(2, even_cnt))

    for i in range(n):
        tmp = (data[i] + (k - 1)) // k
        mv = min(mv, tmp * k - data[i])

    print(mv)