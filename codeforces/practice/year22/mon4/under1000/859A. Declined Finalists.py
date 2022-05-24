import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
print(max(max(data) - 25, 0))