# unsolved

import math
import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return 0
    else:
        return a // b + (a // b // 2 if a % b != 0 else 0) + gcd(b, a % b)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    memo = []
    mv = math.inf
    for i in range(n):
        if a[i] > b[i]:
            cnt = gcd(a[i], b[i])
        else:
            cnt = gcd(b[i], b[i] - a[i]) + 1

        memo.append(cnt)
        mv = min(mv, cnt)

    print(memo)
    if len(set(a)) == 1 and a[0] == 0 or len(set(b)) == 1 and b[0] == 0:
        print("YES")
    else:
        print("YES" if all([(i - mv) % 3 == 0 for i in memo]) else "NO")
