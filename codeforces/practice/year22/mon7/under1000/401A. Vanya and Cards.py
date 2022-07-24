import sys

input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

print((abs(sum(data)) + x - 1) // x)