import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))

    gap = [0] * m
    a += [a[0] + n]
    for i in range(1, m + 1):
        gap[i - 1] = a[i] - a[i - 1] - 1

    sgap = sorted(gap, reverse=True)

    cnt = 0
    days = 0
    # print(sgap)
    for i in sgap:
        tmp = i - days * 2
        # print(days, tmp, end=' ')
        if tmp > 2:
            days += 2
            cnt += tmp - 1
        elif tmp > 1:
            days += 1
            cnt += 1
        elif tmp == 1:
            days += 1
            cnt += 1
        else:
            break
        # print(cnt)

    # print()
    print(n - cnt)