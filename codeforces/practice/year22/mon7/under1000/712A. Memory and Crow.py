import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

print(*([data[i] + data[i + 1] for i in range(n - 1)] + [data[-1]]))