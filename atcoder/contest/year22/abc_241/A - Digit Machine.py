import sys

input = sys.stdin.readline

data = list(map(int, input().split()))
now = 0
for _ in range(3):
    now = data[now]

print(now)