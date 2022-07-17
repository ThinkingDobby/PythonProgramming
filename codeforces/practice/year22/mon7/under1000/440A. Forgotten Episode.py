import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
print(*(set(range(1, n + 1)) - data))