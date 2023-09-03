# RTE, TLE

import collections
import math


def dfs(now, dirs, lev, memo, visited):
    visited[now] = True
    memo[now] = min(memo[now], lev)

    for i in dirs[now]:
        if not visited[i]:
            dfs(i, dirs, memo[now] + 1, memo, visited)
            visited[i] = False


def solution(n, edge):
    dirs = collections.defaultdict(set)

    for s, e in edge:
        dirs[s].add(e)
        dirs[e].add(s)

    memo = [math.inf] * (n + 1)
    visited = [False] * (n + 1)

    memo[0] = 0

    dfs(1, dirs, 0, memo, visited)

    tmp = [memo[i] for i in range(1, len(memo)) if memo[i] != math.inf]
    ans = tmp.count(max(tmp))

    return ans


tmp = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(tmp)
