import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
f = abs(a - b) // 2
s = (abs(a - b) + 1) // 2
print(f * (f + 1) // 2 + s * (s + 1) // 2)