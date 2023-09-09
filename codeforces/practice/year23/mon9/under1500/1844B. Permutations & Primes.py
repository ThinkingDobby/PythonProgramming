import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n < 3:
        print(*range(1, n + 1))
    else:
        memo = [0] * n
        now = 4
        for i in range(1, n - 1):
            if i == n // 2:
                continue

            memo[i] = now
            now += 1

        memo[0] = 2
        memo[-1] = 3
        memo[n // 2] = 1

        print(*memo)