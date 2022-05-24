import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = 0
    l, r = sorted([a[0], b[0]])
    for i in range(1, n):
        x, y = sorted([a[i], b[i]])
        s += abs(l - x) + abs(r - y)
        l = x
        r = y

    print(s)