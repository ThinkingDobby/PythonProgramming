import sys

input = sys.stdin.readline


def quick_sort(data):
    if len(data) <= 1:
        return data

    l, m, r = [], [], []
    p = data[len(data) // 2]

    for i in data:
        if i < p:
            l.append(i)
        elif i > p:
            r.append(i)
        else:
            m.append(i)

    return quick_sort(l) + quick_sort(m) + quick_sort(r)


n = int(input())
data = [int(input()) for _ in range(n)]

print(*quick_sort(data))


"""
3
15
27
12
"""