import sys
inp = sys.stdin.readline


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


ps = get_primes(20000)

for _ in range(int(inp())):
    n = int(inp())

    data = list(map(int, inp().split()))

    s = sum(data)
    if s in ps:
        idx = -1
        for i in range(n):
            if data[i] % 2 == 1:
                idx = i
                break
        print(n - 1)
        print(*[i + 1 for i in range(n) if i != idx])
    else:
        print(n)
        print(*list(range(1, n + 1)))
