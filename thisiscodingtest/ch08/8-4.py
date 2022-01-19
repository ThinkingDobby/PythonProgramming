# 바텀업

def fibo(n):
    data = [0] * 100    # DP 테이블
    data[0], data[1] = 1, 1

    for i in range(2, 100):
        data[i] = data[i - 1] + data[i - 2]

    return data[n - 1]


print(fibo(99))