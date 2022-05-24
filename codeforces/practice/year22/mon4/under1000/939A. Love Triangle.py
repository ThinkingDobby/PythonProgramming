import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

flag = False
for i in range(n):
    a = data[i] - 1
    b = data[a] - 1
    c = data[b] - 1
    if i == c and i != b:
        flag = True
        break

print("YES" if flag else "NO")