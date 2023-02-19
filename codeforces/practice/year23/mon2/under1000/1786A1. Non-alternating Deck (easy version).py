import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    a = 0
    b = 0

    tmp = 1
    for i in range(1, n * 2):
        if a + b + tmp > n:
            if i % 2 == 1:
                a += n - (a + b)
            else:
                b += n - (a + b)
            break

        if i % 2 == 1:
            a += tmp
        else:
            b += tmp

        tmp += 4

    print(a, b)

