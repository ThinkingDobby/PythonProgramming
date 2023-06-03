import sys

input = sys.stdin.readline

n = int(input())
data = sorted(set(map(int, input().split())))

ans = False
for i in range(1, len(data) - 1):
    if data[i - 1] + 1 == data[i] == data[i + 1] - 1:
        ans = True
        break

print("YES" if ans else "NO")
