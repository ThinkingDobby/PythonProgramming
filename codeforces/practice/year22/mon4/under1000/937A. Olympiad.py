import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
print(len(data) if 0 not in data else len(data) - 1)