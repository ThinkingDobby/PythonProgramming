import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

f = data.index(min(data))
s = data.index(max(data))

print(max(f, s, n - f - 1, n - s - 1))