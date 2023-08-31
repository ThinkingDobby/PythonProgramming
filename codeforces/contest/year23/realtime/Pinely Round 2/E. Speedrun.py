# WA

import collections
import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    h = [0] + list(map(int, input().split()))

    c = collections.defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        c[b].append(a)

    smv = math.inf

    for i in range(1, n + 1):
        if i not in c and h[i] < smv:
            smv = h[i]

    mv = 0
    last = max(h)

    for i in range(1, n + 1):
        cnt = 0

        dq = collections.deque()

        lev = 0
        dq.append([i, lev])

        while dq:
            now, lev = dq.popleft()
            for j in c[now]:
                if h[now] < h[j]:
                    dq.append([j, lev + 1])

            if lev > mv:
                mv = lev
                last = h[i]

    print(last, smv, mv)
    ans = k - smv + last + k * (mv - 1)
    print(ans)
