import sys

input = sys.stdin.readline


def upper_bound(data, c):
    l = 1
    r = data[-1] - data[0]

    while l < r:
        mid = (l + r) // 2
        chk = calc(data, mid, c)

        if chk:
            l = mid + 1
        else:
            r = mid

    return r - 1


def calc(data, gap, c):
    cnt = 1
    lim = data[0] + gap

    i = 1
    while i < len(data):
        if data[i] >= lim:
            cnt += 1
            if cnt >= c:
                break
            lim = data[i] + gap
        i += 1

    print(gap, c, lim)
    return cnt >= c and lim >= data[-1]


n, c = map(int, input().split())
data = sorted(int(input()) for _ in range(n))

ans = upper_bound(data, c)
print(ans)

