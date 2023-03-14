import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

inter = sorted(set(a) & set(b))

if len(inter) == 0:
    print(str(a[0]) + str(b[0]) if a[0] < b[0] else str(b[0]) + str(a[0]))
else:
    print(inter[0])