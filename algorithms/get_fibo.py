def get_fibo(cnt, a, b):
    if cnt == 0:
        return a
    else:
        return get_fibo(cnt - 1, b, a + b)
