import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    cntr = collections.Counter(input().rstrip())

    ans = 0
    for i in range(ord('A'), ord('G') + 1):
        tmp = cntr[chr(i)] if chr(i) in cntr else 0
        ans += max(0, m - tmp)

    print(ans)