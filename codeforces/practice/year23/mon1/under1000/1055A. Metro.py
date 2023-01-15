import sys

input = sys.stdin.readline

n, s = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = a[s - 1] == 1

if b[s - 1] == 1:
    for i in range(s - 1, n):
        if a[i] == b[i] == 1:
            ans = True

if a[0] == 0:
    ans = False

print("YES" if ans else "NO")