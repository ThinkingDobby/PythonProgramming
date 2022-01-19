import decimal

h, l = map(decimal.Decimal, input().split())

print((h**2 + l**2) / (2 * h) - h)