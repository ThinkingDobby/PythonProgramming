import sys

input = sys.stdin.readline

n, k, x = map(int, input().split())
data = list(map(int, input().split()))
print(k * x + sum(data[:-k]))