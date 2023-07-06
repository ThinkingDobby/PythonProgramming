import sys

input = sys.stdin.readline

a, b, c, d = map(int, input().split())

f = max(3 * a / 10, a - a / 250 * c)
s = max(3 * b / 10, b - b / 250 * d)

if f == s:
    print("Tie")
else:
    print("Misha" if f > s else "Vasya")