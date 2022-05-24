import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()
f = s = 0
for i in range(1, n):
    if data[i - 1] == 'S' and data[i] == 'F':
        f += 1
    elif data[i - 1] == 'F' and data[i] == 'S':
        s += 1

print("YES" if f > s else "NO")