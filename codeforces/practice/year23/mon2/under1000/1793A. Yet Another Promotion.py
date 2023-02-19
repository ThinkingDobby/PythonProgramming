import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    n, m = map(int, input().split())

    tmp = n // (m + 1)
    print(min(n * b, (n - tmp) * a, tmp * m * a + (n - (tmp * (m + 1))) * b))