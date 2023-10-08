import sys

input = sys.stdin.readline

n = int(input())
data = list(map(lambda x: abs(int(x)), input().split()))

print(min(data))