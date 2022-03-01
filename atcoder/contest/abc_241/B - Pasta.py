import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

memo = {}
for i in a:
    memo[i] = (memo[i] + 1) if i in memo else 1

flag = True
for i in b:
    if i not in memo:
        flag = False
        break
    else:
        if memo[i] <= 0:
            flag = False
            break
        else:
            memo[i] -= 1

if flag:
    print("Yes")
else:
    print("No")