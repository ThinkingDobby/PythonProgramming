def factorial_iterative(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s


def factorial_recursive(n):
    if n == 1:
        return 1
    return factorial_recursive(n - 1) * n


print(factorial_iterative(5))
print(factorial_recursive(5))
