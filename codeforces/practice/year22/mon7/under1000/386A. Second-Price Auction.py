import sys

input = sys.stdin.readline

n = int(input())
data = sorted(zip(map(int, input().split()), range(n)), reverse=True)

print(data[0][1] + 1, data[1][0])