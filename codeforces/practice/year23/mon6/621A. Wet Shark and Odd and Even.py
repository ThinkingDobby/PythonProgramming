import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

s = sum(data)
if s % 2 == 0:
    print(s)
else:
    tmp = min([i for i in data if i % 2 == 1])
    print(s - tmp)