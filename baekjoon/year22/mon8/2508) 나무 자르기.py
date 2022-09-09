import sys

input = sys.stdin.readline


def upper_bound(data, target, _l, _r):
    l = _l
    r = _r

    while l < r:
        mid = (l + r) // 2
        tmp = get_total(mid)
        if tmp >= target:
            l = mid + 1
        else:
            r = mid

    return r - 1


def get_total(lim):
    cnt = 0
    for i in data:
        if i > lim:
            cnt += i - lim

    return cnt


n, m = map(int, input().split())
data = list(map(int, input().split()))
print(upper_bound(data, m, 0, max(data)))
