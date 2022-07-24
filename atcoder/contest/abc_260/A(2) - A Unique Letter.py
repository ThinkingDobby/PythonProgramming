import sys

input = sys.stdin.readline

s = input().rstrip()

ans = False
for i in s:
    if s.count(i) == 1:
        print(i)
        ans = True
        break

if not ans:
    print(-1)