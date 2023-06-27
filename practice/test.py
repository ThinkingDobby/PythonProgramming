def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        if n == 2:
            return True
        else:
            return False
    if n % i == 0:
        return False
    if i * i > n:
        return True

    # Recursive case
    return is_prime(n, i + 1)


def print_sequence(n):
    if n > 1:
        print_sequence(n - 1)
        if is_prime(n):
            print(f'{n} is a prime number.')
        else:
            print(f'{n} is a composite number.')


num = int(input("Enter a single integer: "))
print_sequence(num)
