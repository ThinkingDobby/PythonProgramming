import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    chk = sorted(enumerate(data), key=lambda x: x[1], reverse=True)
    memo = [0] * n

    for i in range(n):
        memo[chk[i][0]] = i + 1

    print(*memo)