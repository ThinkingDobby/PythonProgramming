import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split())) + [1]

ans = []

for i in range(n):
    if data[i + 1] == 1:
        ans.append(data[i])

print(len(ans))
print(*ans)
