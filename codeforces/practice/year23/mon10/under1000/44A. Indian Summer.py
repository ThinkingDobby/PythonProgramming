import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

print(len(set(data)))