import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    s = input().rstrip()

    chk = dict()
    ans = True
    for i in range(n):
        if data[i] not in chk:
            chk[data[i]] = s[i]
        else:
            if chk[data[i]] != s[i]:
                ans = False
                break

    print("YES" if ans else "NO")
