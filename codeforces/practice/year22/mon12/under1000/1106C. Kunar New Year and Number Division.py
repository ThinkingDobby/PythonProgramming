import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))

s = 0
for i in range(n // 2):
    tmp = data[i] + data[-(i + 1)]
    s += tmp * tmp

print(s)

