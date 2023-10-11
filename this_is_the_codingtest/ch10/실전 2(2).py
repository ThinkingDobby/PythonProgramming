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

for t, a, b in data:
    chk = find_parent(parent, a) == find_parent(parent, b)
    if t == 0:
        if not chk:
            union(parent, a, b)
    else:
        print("YES" if chk else "NO")


"""
7 8 
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1 
"""