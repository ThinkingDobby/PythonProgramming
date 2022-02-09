import math

n = int(input())
data = list(map(int, input().split()))
gcd = data[0]
for i in range(1, n):
    gcd = math.gcd(gcd, data[i])
if gcd in data:
    print(gcd)
else:
    print(-1)