import sys

input = sys.stdin.readline

cnt = 1
rank = 1

n = int(input())
data = sorted(zip(map(int, input().split()), list(range(n))), reverse=True)
memo = [0 for _ in range(n)]
memo[data[0][1]] = 1


for i in range(1, n):
    cnt += 1
    if data[i - 1][0] > data[i][0]:
        rank = cnt

    memo[data[i][1]] = rank


print(*memo)
