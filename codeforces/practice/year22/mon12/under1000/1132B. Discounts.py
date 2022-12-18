import sys

input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
m = int(input())
q = list(map(int, input().split()))

s = sum(a)
for i in q:
    print(s - a[i - 1])