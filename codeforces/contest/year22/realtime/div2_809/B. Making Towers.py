# us

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(lambda x: int(x) - 1, input().split()))

    idxs = [-1 for _ in range(n)]
    nows = [0 for _ in range(n)]
    ans = [0 for _ in range(n)]

    for i in range(n):
        if idxs[data[i]] != -1:
            if (i - idxs[data[i]]) % 2 != 1:
                ans[data[i]] = max(ans[data[i]], nows[data[i]])
                nows[data[i]] = 0

        idxs[data[i]] = i
        nows[data[i]] += 1

    print(nows, ans)
    for i in range(n):
        print(max(ans[i], nows[i]), end=' ')
    print()