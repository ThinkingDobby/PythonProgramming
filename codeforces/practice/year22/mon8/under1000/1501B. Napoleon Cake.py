import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    memo = [0] * n

    cnt = data[-1]
    memo[-1] = 1 if cnt else 0
    if cnt > 0:
        cnt -= 1

    for i in range(n - 2, -1, -1):
        cnt = max(data[i], cnt)
        if cnt > 0:
            memo[i] = 1
            cnt -= 1

    print(*memo)