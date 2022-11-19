import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    tmp = 0
    while k != 1 and n // k > 0:
        tmp += n % k
        n //= k
        tmp += 1

    print(n + tmp)