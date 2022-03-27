import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
for i in data:
    if i % 2 == 0:
        print(i - 1, end=' ')
    else:
        print(i, end=' ')