import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))[::-1]
idx0 = n - data.index(0)
idx1 = n - data.index(1)
print(min(idx0, idx1))
