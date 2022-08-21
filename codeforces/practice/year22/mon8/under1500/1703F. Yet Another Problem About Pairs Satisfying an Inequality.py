# us

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    memo = [[a[i], i + 1] for i in range(n) if a[i] < i + 1]
    print(memo)