import sys

input = sys.stdin.readline


def lower_bound(target, _l, _r, x, y):
    l = _l
    r = _r

    while l < r:
        mid = (l + r) // 2
        data = (y + mid) * 100 // (x + mid)
        if data < target:
            l = mid + 1
        else:
            r = mid

    return r


x, y = map(int, input().split())
if x == y:
    print(-1)
else:
    z = y * 100 // x

    tmp = 10**(10**3)
    ans = lower_bound(z + 1, 1, tmp, x, y)
    print(ans if ans != tmp else -1)