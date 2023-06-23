import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = collections.Counter(map(int, input().split()))

    now = 0
    tmp = sorted(data.keys())

    ans = True
    prev = data[0]
    for i in tmp:
        if i != now:
            ans = False
            break

        if data[i] > prev:
            ans = False
            break

        prev = data[i]
        now += 1

    print("YES" if ans else "NO")

