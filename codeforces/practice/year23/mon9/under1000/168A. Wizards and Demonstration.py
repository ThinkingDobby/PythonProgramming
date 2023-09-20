import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

target = (n * y + 99) // 100

print(max(target - x, 0))
