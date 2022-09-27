import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    a = n // k
    b = (n + k - 1) // k

    if a == b:
        print(n)
    else:
        print(n - max(0, n % k - k // 2))
