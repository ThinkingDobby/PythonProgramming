import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    cntr = collections.Counter(data)

    cnt1 = len(cntr)
    chk = set()
    cnt2 = 0

    mv = -1

    for i in range(n):
        cntr[data[i]] -= 1
        if cntr[data[i]] == 0:
            cnt1 -= 1

        if data[i] not in chk:
            chk.add(data[i])
            cnt2 += 1

        mv = max(cnt1 + cnt2, mv)

    print(mv)

