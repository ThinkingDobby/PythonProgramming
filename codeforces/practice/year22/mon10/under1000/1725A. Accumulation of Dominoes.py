import sys

input = sys.stdin.readline

n, m = map(int, input().split())

print(n * (m - 1) if m != 1 else n - 1)