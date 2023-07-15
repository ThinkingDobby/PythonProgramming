# unsolved
# 그래프 색칠 문제

import collections
import sys

input = sys.stdin.readline

n, t, m = map(int, input().split())
check = collections.defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    check[a].add(b)
    check[b].add(a)
