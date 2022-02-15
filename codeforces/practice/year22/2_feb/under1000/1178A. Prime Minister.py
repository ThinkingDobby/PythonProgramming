import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

s = data[0]
ans = [1]
flag = False
for i in range(1, n):
    if data[0] // 2 >= data[i]:
        s += data[i]
        ans.append(i + 1)
    if sum(data) // 2 < s:
        flag = True
        break

if flag:
    print(len(ans))
    print(*ans)
else:
    print(0)