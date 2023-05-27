import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(map(int, input().split()))

    ai = sorted([[a[i], i] for i in range(n)])
    memo = sorted([[ai[i][1], b[i]] for i in range(n)], key=lambda x: x[0])

    for i in range(n):
        print(memo[i][1], end=' ')
    print()
