a1, a2, k1, k2, n = [int(input()) for _ in range(5)]

min_v = 0
max_v = 0

if k2 > k1:
    tmp = min(a1, n // k1)
    max_v = min(a2, (n - k1 * tmp) // k2) + tmp
else:
    tmp = min(a2, n // k2)
    max_v = min(a1, (n - k2 * tmp) // k1) + tmp


tmp = (k1 - 1) * a1 + (k2 - 1) * a2
if n - tmp > 0:
    min_v = min(a1 + a2, n - tmp) if n - tmp > 0 else 0

print(min_v, max_v)