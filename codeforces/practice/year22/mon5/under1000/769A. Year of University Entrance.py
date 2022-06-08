import sys

input = sys.stdin.readline

n = int(input())
data = sorted(map(int, input().split()))
print(data[n // 2])
