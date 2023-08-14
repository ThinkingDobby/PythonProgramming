import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

ecnt = len([i for i in data if i % 2 == 0])

if sum(data) % 2 == 0:
    print(ecnt)
else:
    print(n - ecnt)
