import sys

input = sys.stdin.readline

n = int(int(input()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

f = a[0]
s = b[0]
for i in range(1, n):
    f = f | a[i]
    s = s | b[i]

print(f + s)