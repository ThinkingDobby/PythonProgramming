import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

i = 0
while (sum(data) + k * i) / (n + i) < k - 0.5:
    i += 1

print(i)