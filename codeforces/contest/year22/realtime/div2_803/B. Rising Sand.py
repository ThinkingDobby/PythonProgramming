import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    memo = [-1 for _ in range(n)]

    for i in range(1, n - 1):
        tmp = data[i] - (data[i - 1] + data[i + 1])
        if tmp < 0:
            memo[i] = -1
        elif tmp == 0:
            memo[i] = 0
        elif tmp == 1:
            memo[i] = 1
        else:
            memo[i] = 2

    tot = memo.count(1) + memo.count(2)

    if k == 1:
        if n % 2 == 0:
            print(n // 2 - 1)
        else:
            print(n // 2)
    else:
        print(tot)

