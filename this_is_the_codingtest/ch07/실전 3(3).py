import sys

input = sys.stdin.readline


def upper_bound(data, target, l, r):
    while l < r:
        mid = (l + r) // 2

        cnt = 0
        for i in data:
            cnt += max(i - mid, 0)

        if cnt >= target:
            l = mid + 1
        else:
            r = mid

    return r - 1


n, m = map(int, input().split())
data = list(map(int, input().split()))

ans = upper_bound(data, m, 0, max(data))
print(ans)


"""
4 6
19 15 10 17
"""