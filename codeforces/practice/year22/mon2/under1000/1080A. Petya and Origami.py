import sys

input = sys.stdin.readline

n, k = map(int, input().split())

r = (2 * n + k - 1) // k
g = (5 * n + k - 1) // k
b = (8 * n + k - 1) // k
print(r + g + b)