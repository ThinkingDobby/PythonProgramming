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
    n = int(input())
    divisors = get_divisors(n)

    tmp = divisors[-2]

    print(tmp, n - tmp)
