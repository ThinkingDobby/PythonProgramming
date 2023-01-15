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


n = int(input())
data = list(input().rstrip())
divs = get_divisors(n)

for i in divs:
    data[0:i] = reversed(data[0:i])

print(''.join(data))