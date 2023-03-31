import sys

input = sys.stdin.readline

n = int(input())

data = []
chk = False
for _ in range(n):
    a, b = map(int, input().split())
    if a != b:
        chk = True
    data.append([a, b])

if chk:
    print("rated")
else:
    tmp = [i[0] for i in data]
    if tmp == sorted(tmp, reverse=True):
        print("maybe")
    else:
        print("unrated")