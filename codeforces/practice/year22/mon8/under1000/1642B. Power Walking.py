import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    cnts = collections.Counter(data)

    tmp = len(cnts)
    now = tmp
    for i in range(n):
        print(now, end=' ')
        if i + 1 >= tmp:
            now += 1
    print()