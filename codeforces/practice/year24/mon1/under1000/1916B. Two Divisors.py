import math
import sys

input = sys.stdin.readline


def get_divisors(n):
    i = 1
    divisors = []

    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1

    divisors.sort()
    return divisors


for _ in range(int(input())):
    a, b = map(int, input().split())

    if b % a == 0:
        print(b // a * b)
    else:
        print(a // math.gcd(a, b) * b)