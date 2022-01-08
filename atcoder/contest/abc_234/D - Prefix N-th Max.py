# TLE

import collections


def binary_search(data, target, _l, _r):
    l = _l
    r = _r

    while l < r:
        mid = (l + r + 1) // 2
        if data[mid] < target:
            l = mid
        else:
            r = mid - 1

    return r + 1


n, k = map(int, input().split())
data = list(map(int, input().split()))

q = collections.deque()

for i in sorted(data[:k]):
    q.append(i)
print(q[0])

for i in range(k, n):
    if data[i] > q[0]:
        idx = binary_search(q, data[i], 0, k - 1)
        q.insert(idx, data[i])
        q.popleft()
    print(q[0])