def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:
        return False
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True


v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    ans = union_parent(parent, a, b)
    if not ans:
        print("Cycle Occurred")
        break


"""
3 3
1 2
1 3
2 2
"""