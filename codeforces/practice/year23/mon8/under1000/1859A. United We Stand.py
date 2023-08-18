import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    if len(set(a)) == 1:
        print(-1)
    else:
        tmp = a.index(max(a))
        print(tmp, n - tmp)
        print(*a[:tmp])
        print(*a[tmp:])