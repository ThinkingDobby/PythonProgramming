import math

n = int(input())
data = list(map(int, input().split()))
tmp = data[0]
for i in data[1:]:
    tmp = math.gcd(tmp, i)

print(tmp * n)