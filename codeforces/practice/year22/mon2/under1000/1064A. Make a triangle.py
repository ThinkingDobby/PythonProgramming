import sys

input = sys.stdin.readline

a, b, c = sorted(map(int, input().split()))
print(max(0, c + 1 - (a + b)))
