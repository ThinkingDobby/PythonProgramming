import sys

input = sys.stdin.readline

n = int(input())
memo = {}

for i in range(n):
    data = list(map(int, input().split()))
    memo[data[0]] = data[1]

flag = False
for i in memo.keys():
    if (i + memo[i]) in memo:
        if memo[i + memo[i]] + i + memo[i] == i:
            flag = True
            break

if flag:
    print("YES")
else:
    print("NO")