import collections
import math
import sys

input = sys.stdin.readline

mod = 998_244_353


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
data = list(map(int, input().split()))
primes = [1] + get_primes(n)

chk = collections.defaultdict(int)

for i in range(1, n + 1):
    if i not in primes:
        continue
    mv = -1
    for j in range((n + i - 1) // i, 0, -1):
        print(i, j)
        mv = max(mv, data[j - 1])
        if j > i:
            chk[j] = mv

    chk[i] = mv

ans = 0
schk = sorted(chk.items(), key=lambda x: x[1], reverse=True)
print(schk)
for i in range(1, n + 1):
    ans = (ans + 2**(n - i) * schk[i - 1][1]) % mod

print(ans)