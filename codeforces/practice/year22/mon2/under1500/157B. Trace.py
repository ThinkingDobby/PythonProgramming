import math

n = int(input())
data = sorted(map(int, input().split()), reverse=True) + [0]
s = 0
for i in range(0, n, 2):
    s += (data[i]**2 - data[i + 1]**2) * math.pi

print(s)