import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])
parent = [i for i in range(n + 1)]
memo = []

for f, t, c in edges:
    if find_parent(parent, f) != find_parent(parent, t):
        union(parent, f, t)
        memo.append(c)

print(sum(memo) - max(memo))

"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""