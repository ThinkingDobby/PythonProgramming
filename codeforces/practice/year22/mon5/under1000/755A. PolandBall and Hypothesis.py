import sys
import math

input = sys.stdin.readline


def get_primes(n):
    check = [True for _ in range(0, n + 1)]

    check[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if check[i]:
            for j in range(2 * i, n + 1, i):
                check[j] = False

    primes = [i for i in range(1, n + 1) if check[i]]
    return primes


n = int(input())
data = get_primes(1000000)

for i in range(1, 1000):
    if n * i + 1 not in data:
        print(i)
        break