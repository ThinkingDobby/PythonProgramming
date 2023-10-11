import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    ap = find_parent(parent, a)
    bp = find_parent(parent, b)

    parent[max(ap, bp)] = min(ap, bp)


n, m = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

parent = [i for i in range(n + 1)]

cnt = 0
for f, t, c in edges:
    if find_parent(parent, f) != find_parent(parent, t):
        union(parent, f, t)
        cnt += c

print(cnt)

"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""