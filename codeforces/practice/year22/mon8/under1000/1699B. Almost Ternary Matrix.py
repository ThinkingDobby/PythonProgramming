import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    t = [0, 1, 1, 0]
    f = [1, 0, 0, 1]
    s = [0, 1, 1, 0]
    for i in range(n):
        if t[i % 4] % 2 == 0:
            for j in range(m):
                print(f[j % 4], end=' ')
        else:
            for j in range(m):
                print(s[j % 4], end=' ')
        print()