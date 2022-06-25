import sys

input = sys.stdin.readline

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())

tmp = days[m - 1] - (8 - d)
print((tmp // 7 + (0 if tmp % 7 == 0 else 1)) + 1)