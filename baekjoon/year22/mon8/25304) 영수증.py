import sys

input = sys.stdin.readline

x = int(input())
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print("Yes" if sum([data[i][0] * data[i][1] for i in range(n)]) == x else "No")
