import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    chk = [False] * (n + 1)
    for i in data:
        chk[i] = True

    mex = chk.index(False)

    data = [mex] + data
    s = (-k + 1) % (n + 1)

    for i in range(s, s + n):
        print(data[i % (n + 1)], end=' ')
    print()
