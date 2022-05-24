import sys

input = sys.stdin.readline

c1 = c2 = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 0:
        c1 += 1
    else:
        c2 += 1

if c1 <= 1 or c2 <= 1:
    print("Yes")
else:
    print("No")
