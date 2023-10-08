import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
