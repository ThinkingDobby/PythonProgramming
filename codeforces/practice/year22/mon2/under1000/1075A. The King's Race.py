import sys

input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
a = min(x, y) - 1 + max(x, y) - min(x, y)
b = min(n - x, n - y) + max(x, y) - min(x, y)
if a > b:
    print("Black")
else:
    print("White")