import sys

input = sys.stdin.readline

n = int(input())
print((n // 3) * 2 + (1 if n % 3 != 0 else 0))