import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = input().rstrip()

    cntr = collections.Counter(data)

    cnt = 0
    for i in cntr.values():
        if i % 2 == 1:
            cnt += 1

    print("YES" if cnt <= k + 1 else "NO")
