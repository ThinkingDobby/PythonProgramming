import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
s, t = sorted(map(int, input().split()))

fc = sum(data[s - 1:t - 1])
sc = sum(data[t - 1:]) + sum(data[:s - 1])
print(min(fc, sc))