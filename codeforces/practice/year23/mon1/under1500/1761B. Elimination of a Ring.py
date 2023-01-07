import sys

input = sys.stdin.readline

vows = ['a', 'e', 'i', 'o', 'u']

data = input().rstrip()
ans = data[-1] in vows or data[-1] == 'n'
for i in range(len(data) - 1):
    if data[i] not in vows and data[i + 1] not in vows:
        if data[i] == 'n':
            continue
        ans = False

print("YES" if ans else "NO")