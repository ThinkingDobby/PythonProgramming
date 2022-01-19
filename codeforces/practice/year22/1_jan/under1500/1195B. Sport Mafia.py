import math

n, k = map(int, input().split())
print(n - int(math.sqrt(2 * k + 2 * n + 9 / 4) - 3 / 2))