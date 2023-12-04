import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, x = map(int, input().split())

    tmp = n - k
    ans = k * (k + 1) // 2 <= x <= n * (n + 1) // 2 - tmp * (tmp + 1) // 2

    print("YES" if ans else "NO")

