import sys

input = sys.stdin.readline

n = int(input())
memo = list(map(int, input().split()))
for _ in range(int(input())):
    x, y = map(int, input().split())
    x -= 1

    if n == 1:
        memo[x] = 0
        break

    if x == 0:
        memo[x + 1] += memo[x] - y
    elif x == n - 1:
        memo[x - 1] += y - 1
    else:
        memo[x - 1] += y - 1
        memo[x + 1] += memo[x] - y
    memo[x] = 0

for i in range(n):
    print(memo[i])