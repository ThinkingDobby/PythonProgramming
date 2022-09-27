import sys

input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))

f = sum(data[:n // 2])
s = sum(data[n // 2:])

print(f * f + s * s)