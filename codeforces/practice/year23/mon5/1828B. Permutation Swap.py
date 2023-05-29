import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = [0] * n
    for i in range(n):
        memo[i] = abs(data[i] - (i + 1))

    gcd = memo[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, memo[i])

    print(gcd)