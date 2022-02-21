import math

n = int(input())

s = 0
for i in range(2, n):
    now = n
    while now >= i:
        s += now % i
        now //= i
    s += now

tmp = math.gcd(n - 2, s)
print(str(s // tmp) + '/' + str((n - 2) // tmp))