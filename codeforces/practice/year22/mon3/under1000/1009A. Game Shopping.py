import sys

input = sys.stdin.readline

n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))


j = 0
for i in range(n):
    if c[i] <= a[j]:
        j += 1
        if j >= m:
            break

print(j)