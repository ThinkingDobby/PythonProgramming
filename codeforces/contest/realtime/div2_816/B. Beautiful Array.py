import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, b, s = map(int, input().split())

    if 0 <= s - b * k <= (k - 1) * n:
        cnt = (s - b * k) // (k - 1) if k != 1 else 0
        rest = (s - b * k) % (k - 1) if k != 1 else 0

        memo = [0] * n
        for i in range(n):
            if cnt > 0:
                memo[i] += k - 1
                cnt -= 1
            elif cnt == 0:
                memo[i] += rest
                cnt -= 1

            if i == n - 1:
                memo[i] += b * k
        print(*memo)
    else:
        print(-1)
