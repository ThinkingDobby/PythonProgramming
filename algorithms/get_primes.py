import math


def get_primes(n):
    check = [True for _ in range(0, n + 1)]

    check[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if check[i]:
            for j in range(2 * i, n + 1, i):
                check[j] = False

    primes = [i for i in range(1, n + 1) if check[i]]
    return primes


print(get_primes(int(input())))