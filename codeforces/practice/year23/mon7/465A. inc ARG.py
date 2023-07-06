import sys

input = sys.stdin.readline

n = int(input())
data = input().rstrip()[::-1]
tmp = bin(int(data, 2) + 1)[2:]
tmp = (n - len(tmp)) * '0' + tmp

cnt = 0
for i in range(n):
    if data[-(i + 1)] != tmp[-(i + 1)]:
        cnt += 1

print(cnt)
