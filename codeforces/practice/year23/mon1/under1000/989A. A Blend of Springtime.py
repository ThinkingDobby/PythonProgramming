import sys

input = sys.stdin.readline

data = input().rstrip()

ans = False
for i in range(1, len(data) - 1):
    if {data[i], data[i - 1], data[i + 1]} == {'A', 'B', 'C'}:
        ans = True
        break

print("YES" if ans else "NO")