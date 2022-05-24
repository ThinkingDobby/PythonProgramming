# WA

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [input().rstrip() for _ in range(n)]

    memo = list(filter(lambda x: x != -1, [i.find('R') for i in data]))
    print("YES" if memo == sorted(memo) else "NO")