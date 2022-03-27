import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in x:
    if i in y:
        print(i, end=' ')