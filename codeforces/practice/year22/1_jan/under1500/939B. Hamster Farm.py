import math

n, k = map(int, input().split())
data = list(map(int, input().split()))

midx = -1
mv = math.inf
for i in range(k):
    if n % data[i] < mv:
        mv = n % data[i]
        midx = i

print(midx + 1, n // data[midx])