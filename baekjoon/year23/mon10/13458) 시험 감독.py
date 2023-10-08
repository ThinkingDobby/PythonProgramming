import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(n):
    cnt += 1
    cnt += (max(0, a[i] - b) + c - 1) // c

print(cnt)
