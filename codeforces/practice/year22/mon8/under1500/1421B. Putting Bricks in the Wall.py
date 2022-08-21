import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip() for _ in range(n)]

    memo = {(1, 2): data[0][1], (2, 1): data[1][0], (n, n - 1): data[n - 1][n - 2], (n - 1, n): data[n - 2][n - 1]}
    if memo[(1, 2)] == memo[(2, 1)] == memo[(n, n - 1)] == memo[(n - 1, n)]:
        print(2)
        print(1, 2)
        print(2, 1)
    elif memo[(1, 2)] == memo[(2, 1)] and memo[(n, n - 1)] == memo[(n - 1, n)]:
        print(0)
    elif memo[(1, 2)] == memo[(2, 1)]:
        if memo[(n, n - 1)] == memo[(1, 2)]:
            print(1)
            print(n, n - 1)
        else:
            print(1)
            print(n - 1, n)
    elif memo[(n, n - 1)] == memo[(n - 1, n)]:
        if memo[(n, n - 1)] == memo[(1, 2)]:
            print(1)
            print(1, 2)
        else:
            print(1)
            print(2, 1)
    else:
        if memo[(n, n - 1)] == memo[(1, 2)]:
            print(2)
            print(1, 2)
            print(n - 1, n)
        else:
            print(2)
            print(2, 1)
            print(n - 1, n)