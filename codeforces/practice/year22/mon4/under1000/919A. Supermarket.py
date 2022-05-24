import decimal
import sys

input = sys.stdin.readline


def func(a):
    return a[0] / a[1]


n, m = map(int, input().split())
print(min([func(list(map(decimal.Decimal, input().split()))) for n in range(n)]) * m)
