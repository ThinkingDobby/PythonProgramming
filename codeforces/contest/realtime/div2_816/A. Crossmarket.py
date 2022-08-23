import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = sorted(map(int, input().split()))
    if n == 1:
        print(m if m != 1 else 0)
    else:
        print(n * 2 + m - 2)