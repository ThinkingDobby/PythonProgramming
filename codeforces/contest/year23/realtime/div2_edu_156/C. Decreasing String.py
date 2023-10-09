# WA
# 반례: hdgcf

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()
    pos = int(input())

    n = len(data)

    sizes = [0] * n
    sizes[0] = n
    for i in range(1, n):
        sizes[i] = sizes[i - 1] + n - i
    sizes = [0] + sizes

    section = -1
    sidx = -1
    for i in range(1, n + 1):
        if sizes[i - 1] < pos <= sizes[i]:
            section = i # section은 1부터
            sidx = pos - sizes[i - 1] - 1 # sidx는 0부터
            break

    memo = [0] * n

    i = 1
    now = 1
    if n > 2:
        while data[i - 1] > data[i]:
            memo[i - 1] = now
            now += 1
            i += 1
            if i >= n:
                break

    memo[i - 1] = n
    for j in sorted(enumerate(data[i:]), key=lambda x: x[1], reverse=True):
        memo[j[0] + i] = now
        now += 1

    print(memo)
    ans = [data[i] for i in range(n) if memo[i] >= section][sidx]
    print(ans, end='')



