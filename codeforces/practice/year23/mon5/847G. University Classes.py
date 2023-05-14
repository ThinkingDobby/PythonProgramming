import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().rstrip())) for _ in range(n)]

mv = -1
for i in range(7):
    mv = max(mv, [data[j][i] for j in range(n)].count(1))

print(mv)