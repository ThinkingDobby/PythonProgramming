import sys

input = sys.stdin.readline

s = sorted(input().rstrip())
print(s[-1] * s.count(s[-1]))