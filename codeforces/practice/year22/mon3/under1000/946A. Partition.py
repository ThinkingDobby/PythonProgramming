import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

f = 0
s = 0
for i in data:
    if i > 0:
        f += i
    else:
        s += i

print(f - s)