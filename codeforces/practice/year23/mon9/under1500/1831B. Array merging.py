import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split())) + [-1]
    b = list(map(int, input().split())) + [-1]

    acnts = collections.defaultdict(int)
    bcnts = collections.defaultdict(int)

    acnt = 1
    bcnt = 1
    for i in range(1, n + 1):
        if a[i - 1] != a[i]:
            acnts[a[i - 1]] = max(acnts[a[i - 1]], acnt)
            acnt = 1
        else:
            acnt += 1

        if b[i - 1] != b[i]:
            bcnts[b[i - 1]] = max(bcnts[b[i - 1]], bcnt)
            bcnt = 1
        else:
            bcnt += 1

    sums = {key: (acnts[key] + bcnts[key]) for key in set(acnts.keys()) | set(bcnts.keys())}

    print(max(sums.values()))
