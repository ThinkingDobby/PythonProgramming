import sys

input = sys.stdin.readline

a, b, c = [int(input()) for _ in range(3)]
print(min(a, b // 2, c // 4) * 7)