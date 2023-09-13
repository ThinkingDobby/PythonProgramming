import sys
from functools import lru_cache

# 기본 recursion limit은 1000
# 너무 높게 (ex: 1e7) 설정 시 메모리 오류 발생함에 주의
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
#     if cnt <= 0:
#         return a
#     else:
#         return get_fibo(cnt - 1, b, a + b)
