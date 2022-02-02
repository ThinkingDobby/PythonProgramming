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


v, e = map(int, input().split())
edges = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
for i in edges:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        result += i[0]
        union_parent(parent, i[1], i[2])

print(result)
