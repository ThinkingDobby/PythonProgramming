import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    print(n if k < n - 1 else 1)