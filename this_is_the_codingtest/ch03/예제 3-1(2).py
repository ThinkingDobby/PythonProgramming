import sys

input = sys.stdin.readline

n = int(input())

coins = [500, 100, 50, 10]

now = n
cnt = 0
for i in coins:
    cnt += now // i
    now %= i

print(cnt)