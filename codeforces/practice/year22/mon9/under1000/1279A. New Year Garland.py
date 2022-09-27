import sys

input = sys.stdin.readline

for _ in range(int(input())):
    r, g, b = map(int, input().split())
    print("NO" if max(r, g, b) - 1 > r + g + b - max(r, g, b) else "YES")