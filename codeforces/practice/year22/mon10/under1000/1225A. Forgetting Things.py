import sys

input = sys.stdin.readline

a, b = map(int, input().split())
if b - a == 1:
    print(a, b)
elif b - a == 0:
    print(10 * a, 10 * b + 1)
elif a == 9 and b == 1:
    print(9, 10)
else:
    print(-1)
