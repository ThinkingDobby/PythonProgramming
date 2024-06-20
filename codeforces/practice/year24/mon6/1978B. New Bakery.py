import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    k = min(n, b - a + 1)
    if k < 0:
        print(n * a)
    else:
        print((b + 1) * k - k * (k + 1) // 2 + (n - k) * a)
