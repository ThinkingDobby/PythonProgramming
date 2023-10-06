import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, x = map(int, input().split())

    if n < k or k > x + 1:
        print(-1)
    else:
        ans = k * (k - 1) // 2 + (n - k) * (k - 1 if x == k else x)
        print(ans)