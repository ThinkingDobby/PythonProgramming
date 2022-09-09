import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = sorted(map(int, input().split()), reverse=True)
print(data[k - 1])