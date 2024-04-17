import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n = list(map(int, input().split()))

    for i in range(q):
        print(min(n[i], a[0] - 1), end=' ')

    print()
