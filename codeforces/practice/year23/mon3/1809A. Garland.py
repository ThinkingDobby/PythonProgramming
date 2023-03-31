import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    s = collections.Counter(map(int, data))

    mv = max(s.values())
    n = len(data)

    tmp = n - mv + 1

    if mv == n:
        print(-1)
    else:
        if mv > (n + 1) // 2:
            ans = tmp + (mv - tmp) * 2 + (2 if (mv - tmp) % 2 == 1 else 1)
            print(ans)
        else:
            print(n)
