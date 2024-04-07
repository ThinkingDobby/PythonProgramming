import collections
import sys

input = sys.stdin.readline


def union(parent, a, b, cnts):
    pa = find(parent, a)
    pb = find(parent, b)

    if pa > pb:
        parent[pa] = pb
        cnts[pb] += cnts[pa]
        return cnts[pb]
    elif pa < pb:
        parent[pb] = pa
        cnts[pa] += cnts[pb]
        return cnts[pa]
    else:
        return cnts[pa]


def find(parent, a):
    if parent[a] == a:
        return a
    else:
        return find(parent, parent[a])


for _ in range(int(input())):
    cnts = collections.defaultdict(int)
    mapping = dict()
    parent = dict()

    idx = 0

    for _ in range(int(input())):
        a, b = input().split()

        if a not in mapping:
            mapping[a] = idx
            parent[idx] = idx
            cnts[idx] += 1
            idx += 1

        if b not in mapping:
            mapping[b] = idx
            parent[idx] = idx
            cnts[idx] += 1
            idx += 1

        ans = union(parent, mapping[a], mapping[b], cnts)

        print(ans)
