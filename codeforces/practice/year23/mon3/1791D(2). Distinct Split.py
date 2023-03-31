# unsolved

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    mv = -1
    chk = set()
    for i in range(1, n):
        if data[i] not in chk:
            mv = max(mv, len(set(data[:i])) + len(set(data[i:])))
            chk.add(data[i])

    print(mv)