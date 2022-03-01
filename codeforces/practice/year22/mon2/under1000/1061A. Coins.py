import sys

input = sys.stdin.readline

n, s = map(int, input().split())
print((s + n - 1) // n)