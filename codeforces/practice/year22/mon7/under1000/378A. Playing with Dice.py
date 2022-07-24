import sys

input = sys.stdin.readline

a, b = map(int, input().split())

f = 0
s = 0
t = 0
for i in range(1, 7):
    x = abs(a - i)
    y = abs(b - i)
    if x < y:
        f += 1
    elif x == y:
        s += 1
    else:
        t += 1

print(f, s, t)