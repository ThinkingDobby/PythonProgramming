import sys

input = sys.stdin.readline

n = int(input())

if n == 20:
    print(15)
elif 11 <= n <= 21:
    print(4)
else:
    print(0)