import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = input().rstrip()

    dp = [0] * n
    dp[n - 1] = 1 if data[n - 1] == 'B' else 0
    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + 1] + (1 if data[i] == 'B' else 0)

    if k == dp[0]:
        print(0)
    else:
        dp += [0]
        for i in range(n):
            if dp[i + 1] + i + 1 == k:
                print(1)
                print(i + 1, 'B')
                break
            elif dp[i + 1] == k:
                print(1)
                print(i + 1, 'A')
                break
