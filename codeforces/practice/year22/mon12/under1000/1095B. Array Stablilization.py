import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))

if n == 2:
    print(0)
else:
    print(min(data[-1] - data[0], data[-1] - data[1], data[-2] - data[0]))