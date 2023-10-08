import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())

    if n >= m:
        if k == 1:
            print(1)
        elif k == 2:
            print(m)
        else:
            print(0)
    else:
        cnt1 = 1
        cnt2 = n - 1

        tmp = m // n
        cnt2 += tmp
        cnt3 = m - n - tmp + 1

        if k == 1:
            print(cnt1)
        elif k == 2:
            print(cnt2)
        elif k == 3:
            print(cnt3)
        else:
            print(0)