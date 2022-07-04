def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
graph = []
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
s = 0
mv = -1
for cost, a, b in graph:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        union_parent(parent, a, b)
        s += cost
        mv = max(mv, cost)

print(s - mv)

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