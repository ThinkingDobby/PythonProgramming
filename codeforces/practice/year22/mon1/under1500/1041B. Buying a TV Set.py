import math

a, b, x, y = map(int, input().split())

gcd = math.gcd(x, y)
print(min(a // (x // gcd), b // (y // gcd)))