import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()

    cnts = dict(collections.Counter(b))
    chk = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] in cnts and cnts[a[i]] != 0:
            cnts[a[i]] -= 1
            chk.append(a[i])

    print("YES" if ''.join(chk[::-1]) == b else "NO")
