import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
print(len(data) + (-1 if 0 in data else 0))