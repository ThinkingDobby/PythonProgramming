import sys

input = sys.stdin.readline

n = int(input())
if n % 2 == 0:
    if (n // 2) % 2 == 1:
        print(n // 2 - 2, n // 2 + 2)
    else:
        print(n // 2 - 1, n // 2 + 1)
else:
    print(n // 2, n // 2 + 1)
