import itertools
import math


def solution(n, weak, dist):
    cases = list(itertools.permutations(dist, len(dist)))
    c_weak = weak + list(map(lambda x: x + n, weak))

    ans = math.inf
    for case in cases:
        for i in range(len(weak) + 1):
            j = 0
            while True:
                tmp = c_weak[i] + case[j]
                for k in range(i, i + len(weak)):
                    if c_weak[k] > tmp:
                        j += 1
                        if j >= len(dist):
                            break
                        tmp = c_weak[k] + case[j]
                    if k == i + len(weak) - 1 and c_weak[k] <= tmp:
                        ans = min(ans, j + 1)
                break

    return -1 if ans == math.inf else ans


ans = solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
print(ans)