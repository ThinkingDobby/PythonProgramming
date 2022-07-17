import sys
from functools import lru_cache

sys.setrecursionlimit(int(1e5))

# lru_cache: 자동으로 함수 결과 저장
@lru_cache()
def get_fibo(n):
    if n < 2:
        return n
    else:
        return get_fibo(n - 1) + get_fibo(n - 2)


# print(get_fibo(1000, 0, 1))
print(get_fibo(1000))

# def get_fibo(cnt, a, b):
#     if cnt == 0:
#         return a
#     else:
#         return get_fibo(cnt - 1, b, a + b)
