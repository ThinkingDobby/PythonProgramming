import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
for i in range(max(data), max(data) * 2 + 2):
    cnt = 0
    for j in range(n):
        cnt += max(0, i - data[j])
    if cnt > sum(data):
        print(i)
        break