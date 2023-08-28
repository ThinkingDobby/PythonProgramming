import math


# 시간 기준으로 lower bound
def lower_bound(l, r, target, data):
    while l < r:
        mid = (l + r) // 2

        s = 0

        for i in data:
            s += mid // i   # 사람 수 계산

        if s < target:
            l = mid + 1
        else:
            r = mid

    return r


def solution(n, times):
    ans = math.inf
    ans = min(ans, lower_bound(1, 10**18, n, times))

    return ans


print(solution(6, [7, 10]))