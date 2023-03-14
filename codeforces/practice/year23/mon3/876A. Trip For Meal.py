import sys

input = sys.stdin.readline

n = int(input())
a, b, c = [int(input()) for _ in range(3)]

mv = min(a, b, c)
if n == 1:
    print(0)
elif mv == a or mv == b:
    print(mv * (n - 1))
else:
    print(min(a, b) + mv * (n - 2))