import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    s = 0
    tot = 0
    memo = [[] for _ in range(n)]
    for i in range(n):
        cnt = 0
        tmp = data[i]
        while tmp % 2 == 0:
            tmp //= 2
            cnt += 1
        memo[i] = [tmp, cnt]
        s += tmp
        tot += cnt

    mv = -1
    for i in range(n):
        mv = max(mv, s - memo[i][0] + data[i] * 2**(tot - memo[i][1]))

    print(mv)
