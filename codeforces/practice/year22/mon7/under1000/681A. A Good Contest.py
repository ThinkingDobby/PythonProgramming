import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split()[1:])) for _ in range(n)]

ans = False
for i in data:
    if 2400 <= i[0] < i[1]:
        ans = True
        break

print("YES" if ans else "NO")