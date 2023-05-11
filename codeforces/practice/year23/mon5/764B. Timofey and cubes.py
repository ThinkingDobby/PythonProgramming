import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

for i in range((n + 1) // 2):
    if i % 2 == 0:
        data[i], data[-(i + 1)] = data[-(i + 1)], data[i]

print(*data)
