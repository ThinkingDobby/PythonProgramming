# 참조한 코드

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, c, q = map(int, input().split())
    data = input().rstrip()

    left = [0] * (c + 1)
    right = [0] * (c + 1)
    diff = [0] * (c + 1)

    left[0] = 0
    right[0] = n

    for i in range(1, c + 1):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        left[i] = right[i - 1]
        right[i] = left[i] + (r - l + 1)
        diff[i] = left[i] - l
        # print(left, right, diff)

    for _ in range(q):
        k = int(input())
        k -= 1
        for i in range(c, 0, -1):
            if k < left[i]:
                continue
            else:
                k -= diff[i]

        print(data[k])
