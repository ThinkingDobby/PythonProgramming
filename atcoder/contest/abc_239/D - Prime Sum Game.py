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


primes = get_primes(200)
ans = True

a, b, c, d = map(int, input().split())

for i in range(a, b + 1):
    flag = False
    for j in range(c, d + 1):
        if i + j in primes:
            flag = True
            break
    if not flag:
        ans = False
        break

if ans:
    print("Aoki")
else:
    print("Takahashi")

