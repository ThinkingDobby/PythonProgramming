import sys

input = sys.stdin.readline

n = int(input())
data = sorted(enumerate(map(int, input().split())), key=lambda x: x[1], reverse=True)

s = 0
for i in range(n):
    s += data[i][1] * i + 1
print(s)

print(*[i[0] + 1 for i in data])