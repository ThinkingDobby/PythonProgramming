import math

mv = math.inf

n, m, a, b = map(int, input().split())
mv = min(mv, n % m * b, (-n) % m * a)
print(mv)