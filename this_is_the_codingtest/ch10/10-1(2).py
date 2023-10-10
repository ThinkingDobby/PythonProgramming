import sys

input = sys.stdin.readline


def find_parent(parent, now):
    while parent[now] != now:
        now = parent[now]

    return now


def union(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)

    if parent_a != parent_b:
        parent[max(parent_a, parent_b)] = min(parent_a, parent_b)


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

for i in range(1, n + 1):
    print(find_parent(parent, i), end=' ')
print()
print(*parent[1:])