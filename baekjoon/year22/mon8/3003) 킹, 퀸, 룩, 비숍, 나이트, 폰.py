import sys

input = sys.stdin.readline

memo = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split()))
print(*[(memo[i] - data[i]) for i in range(6)])