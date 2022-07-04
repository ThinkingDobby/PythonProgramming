import sys

input = sys.stdin.readline

data = input().rstrip()
ans = set()

for i in range(1, len(data) + 1):
    for j in range(0, len(data) - i + 1):
        ans.add(data[j:j + i])

print(len(ans))