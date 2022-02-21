import math

n = int(input())
a = int(math.sqrt(n))
b = a
if a * a < n:
    b += 1
    if a * b < n:
        a += 1

print((a + b) * 2)
