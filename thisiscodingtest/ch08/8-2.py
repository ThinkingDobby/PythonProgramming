# 탐다운

memo = [0] * 100    # 메모이제이션 기법


def fibo(n):
    if n == 1 or n == 2:
        return 1

    if memo[n] != 0:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


print(fibo(99))