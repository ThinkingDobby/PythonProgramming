# WA

import math


# 사람 수 기준으로 lower bound
def lower_bound(l, r, target, data, mv):
    ans = math.inf

    while l < r:
        mid = (l + r) // 2

        s = 0
        base = mv * mid # 사람 수 기준으로 시간 계산

        for i in data:
            tmp = base // i
            s += tmp

        if s < target:
            l = mid + 1
        else:
            r = mid

        if s >= target:
            ans = min(ans, base)

    return ans


def solution(n, times):
    ans = math.inf
    ans = min(ans, lower_bound(1, 1_000_000_000, n, times, min(times)))

    return ans


print(solution(7, [2, 34, 13]))

# 예외
# print(solution(7, [2, 34, 13])) # 13
# print(solution(5, [5, 6, 7])) # 12

