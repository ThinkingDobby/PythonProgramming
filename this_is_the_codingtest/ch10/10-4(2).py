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
data = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]

for f, t in data:
    if find_parent(parent, f) == find_parent(parent, t):
        print("Cycle")
        break
    else:
        union(parent, f, t)

"""
3 3
1 2
1 3
2 2
"""