import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = abs(int(input()))
    if n == 1:
        print(2)
    else:
        print(n // 3 + (1 if n % 3 else 0))