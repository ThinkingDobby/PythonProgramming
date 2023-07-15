import decimal
import math
import sys

input = sys.stdin.readline


def rad_to_deg(r):
    return (r * 180) / math.pi


def deg_to_rad(d):
    return (d * decimal.Decimal(math.pi)) / 180


a, b, d = map(decimal.Decimal, input().split())
rad = math.atan2(b, a)
deg = rad_to_deg(rad)
l = math.sqrt(a**2 + b**2)

n_deg = deg_to_rad(decimal.Decimal(deg) + d)
print(l * math.cos(n_deg), l * math.sin(n_deg))
