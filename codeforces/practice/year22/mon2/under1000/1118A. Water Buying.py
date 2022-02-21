import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print(min(a * n, (n // 2) * b + (a if n % 2 == 1 else 0)))