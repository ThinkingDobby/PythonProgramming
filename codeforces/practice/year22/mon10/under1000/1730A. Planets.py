import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, c = map(int, input().split())
    cnts = dict(collections.Counter(map(int, input().split())))

    s = 0
    for i in cnts.keys():
        s += min(cnts[i], c)

    print(s)