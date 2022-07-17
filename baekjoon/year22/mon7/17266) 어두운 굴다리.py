import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))
mv = max(data[0] - 0, n - data[-1])
for i in range(1, m):
    mv = max(mv, (data[i] - data[i - 1] + 1) // 2)
print(mv)