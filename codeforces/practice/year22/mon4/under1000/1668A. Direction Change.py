import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 2 * (min(n, m) - 1) + (abs(n - m) * 2 if abs(n - m) % 2 == 0 else abs(n - m) * 2 - 1)
    if n == 1 and m > 2 or n > 2 and m == 1:
        print(-1)
    else:
        print(ans)