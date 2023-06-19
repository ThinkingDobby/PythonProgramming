import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    if n % k == 0:
        print(2)
        print(n + 1,  -1)
    else:
        print(1)
        print(n)
