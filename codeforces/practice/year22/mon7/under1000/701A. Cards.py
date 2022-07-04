import sys

input = sys.stdin.readline

n = int(input())
data = sorted(zip(list(range(n)), list(map(int, input().split()))), key=lambda x: x[1])

for i in range(n // 2):
    print(data[i][0] + 1, data[-(i + 1)][0] + 1)