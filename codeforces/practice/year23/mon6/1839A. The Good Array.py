# unsolved

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    cnt = ((n // 2) + k - 1) // k * 2
    if n % 2 == 1:
        if (n // 2) % k == 0:
            cnt += 1

    print(cnt)