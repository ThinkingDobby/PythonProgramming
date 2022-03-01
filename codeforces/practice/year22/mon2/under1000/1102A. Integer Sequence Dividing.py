import sys

input = sys.stdin.readline

n = int(input())
print(1 if n % 4 in (1, 2) else 0)