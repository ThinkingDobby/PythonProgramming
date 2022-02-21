import math

n = int(input())

sq = int(math.sqrt(n * 2))
if n * 2 <= sq * (sq + 1):
    sq -= 1

print(n - sq * (sq + 1) // 2)