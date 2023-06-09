import sys

input = sys.stdin.readline

n = int(input())
p = int(input())
q = int(input())

print(p / (p + q) * n)