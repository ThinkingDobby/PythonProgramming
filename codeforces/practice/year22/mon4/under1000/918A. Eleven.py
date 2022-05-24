import sys
from functools import lru_cache

input = sys.stdin.readline


@lru_cache()
def get_fibo(n):
    if n < 2:
        return n
    else:
        return get_fibo(n - 1) + get_fibo(n - 2)


fibos = []
for i in range(1, 1000):
    tmp = get_fibo(i)
    if tmp > 1000:
        break
    fibos.append(tmp)

n = int(input())
print("".join(['O' if (i + 1) in fibos else 'o' for i in range(n)]))