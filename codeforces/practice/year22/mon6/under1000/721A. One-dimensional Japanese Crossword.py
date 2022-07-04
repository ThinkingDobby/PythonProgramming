import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()

data += 'W'
cnt = 0 if data[0] == 'W' else 1
ans = []
for i in range(1, n + 1):
    if data[i] == 'B':
        cnt += 1
    elif data[i - 1] == 'B':
        ans.append(cnt)
        cnt = 0

print(len(ans))
print(*ans)
