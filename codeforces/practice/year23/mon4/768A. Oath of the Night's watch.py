import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

max_v = max(data)
min_v = min(data)
print(len([i for i in data if min_v < i < max_v]))