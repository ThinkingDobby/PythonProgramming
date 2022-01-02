def get_primes(n):
    check = [True for _ in range(0, n + 1)]
    primes = []

    check[0] = check[1] = False
    for i in range(2, n + 1):
        if check[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                check[j] = False
    return primes