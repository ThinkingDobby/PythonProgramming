import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    cnts = dict(collections.Counter(data))
    ccnts = {i:cnts[i] for i in cnts if cnts[i] != 1}

    tmp = len(ccnts)
    ans = 0
    if tmp == 0:
        print(0)
    else:
        for i in range(n):
            ans += 1
            if data[i] in ccnts:
                ccnts[data[i]] -= 1
                if ccnts[data[i]] == 1:
                    tmp -= 1
                if tmp <= 0:
                    break

        print(ans)