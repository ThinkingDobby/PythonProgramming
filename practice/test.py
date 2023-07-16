def count_iterations(a, b):
    cnt = 0
    while b != 0:
        if a > b:
            cnt += a // b
            a %= b
        else:
            a, b = b, abs(a - b)
            cnt += 1
    return cnt

a = int(input())
b = int(input())
print(count_iterations(a, b))
