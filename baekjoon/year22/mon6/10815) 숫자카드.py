import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
m = int(input())
memo = list(map(int, input().split()))

for i in memo:
    print(1 if i in data else 0, end=' ')
