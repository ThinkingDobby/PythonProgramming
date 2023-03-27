import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    for i in range(m):
        mi = a.index(min(a))
        a[mi] = b[i]

    print(sum(a))

