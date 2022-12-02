import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(*([4] * (n - 2) + [6, 2]))
    else:
        print(*([1] * n))
