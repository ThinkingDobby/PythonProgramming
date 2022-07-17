import decimal
import sys

input = sys.stdin.readline

d, l, v1, v2 = map(decimal.Decimal, input().split())
print((l - d) / (v1 + v2))