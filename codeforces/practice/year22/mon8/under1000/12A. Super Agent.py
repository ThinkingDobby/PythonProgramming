import sys

input = sys.stdin.readline

data = [input().rstrip() for _ in range(3)]

ans = True
for i in range(3):
    if data[0][i] != data[2][3 - i - 1]:
        ans = False

if data[1][0] != data[1][2]:
    ans = False

print("YES" if ans else "NO")