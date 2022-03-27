import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
ans = []
for i in data[::-1]:
    if i not in ans:
        ans.append(i)

print(len(ans))
print(*ans[::-1])