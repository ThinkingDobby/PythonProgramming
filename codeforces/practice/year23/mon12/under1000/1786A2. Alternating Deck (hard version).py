import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    flag = 0
    chk = False
    gap = 2
    flag_cnt = 0

    cnt = [0] * 4
    cnt[0] = 1  # A - WB B - WB

    for i in range(1, n):
        if chk:
            if i % 2 == 0:
                cnt[0] += 1
            else:
                cnt[1] += 1
        else:
            if i % 2 == 0:
                cnt[2] += 1
            else:
                cnt[3] += 1

        flag += 1
        if flag >= gap:
            gap += 1
            flag = 0
            flag_cnt += 1
            if flag_cnt >= 2:
                chk = not chk
                flag_cnt = 0

    print(*cnt)