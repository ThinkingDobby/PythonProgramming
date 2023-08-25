import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [min(map(int, input().split())) for _ in range(n)]

print(max(data))