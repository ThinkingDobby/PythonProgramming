# unsolved

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split())) + [-1]

    tmp = 0
    know = 0
    cnt = 0
    for i in range(n + 1):
        if data[i] == 2:
            if tmp != 0:
                cnt += tmp // 2 + 1
                if know >= 2:
                    know = 0
                    cnt -= 1
                know += 1 if tmp % 2 else 2
                tmp = 0
        elif data[i] == 1:
            tmp += 1
        else:
            cnt += tmp
            if know >= 2:
                know = 0
                cnt -= 1
        print(i, cnt, know)

    print(cnt)