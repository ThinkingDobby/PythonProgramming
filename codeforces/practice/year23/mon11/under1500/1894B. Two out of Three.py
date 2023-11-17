import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    cntr = collections.Counter(data)
    chk = [i for i in cntr if cntr[i] > 1]

    if len(chk) < 2:
        print(-1)
    else:
        f = chk[0]
        s = chk[1]

        fc = False
        sc = False

        ans = []
        for i in range(n):
            if data[i] == f:
                if fc:
                    ans.append(2)
                else:
                    fc = True
                    ans.append(1)
            elif data[i] == s:
                if sc:
                    ans.append(3)
                else:
                    sc = True
                    ans.append(1)
            else:
                ans.append(1)

        print(*ans)
