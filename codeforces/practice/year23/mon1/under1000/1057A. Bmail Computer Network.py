import sys

input = sys.stdin.readline

n = int(input())
data = [-1, 0] + list(map(int, input().split()))

now = n
ans = []
while data[now] != -1:
    ans.append(now)
    now = data[now]

print(*reversed(ans))
