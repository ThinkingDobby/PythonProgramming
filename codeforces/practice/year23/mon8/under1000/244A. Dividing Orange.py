import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

check = [False] * (n * k + 1)
for i in range(k):
    check[a[i]] = True

now = 1
for i in range(k):
    print(a[i], end=' ')
    for j in range(n - 1):
        while check[now]:
            now += 1
        check[now] = True
        print(now, end=' ')

    now += 1
    print()
