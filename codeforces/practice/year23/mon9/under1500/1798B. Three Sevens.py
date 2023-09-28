import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    check = collections.defaultdict(int)

    for now in range(1, m + 1):
        n = int(input())
        data = list(map(int, input().split()))

        for i in data:
            check[i] = now

    if set(check.values()) == set([i for i in range(1, m + 1)]):
        tmp = dict()
        for i in check:
            tmp[check[i]] = i
        for i in range(1, m + 1):
            print(tmp[i], end=' ')
        print()
    else:
        print(-1)