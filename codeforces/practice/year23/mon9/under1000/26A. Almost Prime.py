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


def get_primes(n):
    check = [True for _ in range(0, n + 1)]

    check[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if check[i]:
            for j in range(2 * i, n + 1, i):
                check[j] = False

    primes = [i for i in range(1, n + 1) if check[i]]
    return primes


memo = set(get_primes(3000))


n = int(input())
cnt = 0

for i in range(1, n + 1):
    if len(set(get_divisors(i)) & memo) == 2:
        cnt += 1

print(cnt)
