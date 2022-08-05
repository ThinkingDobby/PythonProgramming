import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())
data = sorted(map(int, input().split()))

print(data[b] - data[b - 1])
