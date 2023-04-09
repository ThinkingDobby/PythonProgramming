import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)

j = 0
for i in range(n):
    if a[i] == 0:
        a[i] = b[j]
        j += 1

print("No" if a == sorted(a) else "Yes")
