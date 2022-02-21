import math

for _ in range(int(input())):
    n = int(input())

    while True:
        if math.gcd(n, sum(list(map(int, str(n))))) != 1:
            print(n)
            break
        n += 1
