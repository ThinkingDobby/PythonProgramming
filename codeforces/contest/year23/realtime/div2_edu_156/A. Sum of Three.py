import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n <= 6 or n == 9:
        print("NO")
    else:
        a = 1
        b = 2
        c = n - 3

        if c % 3 == 0:
            b += 2
            c -= 2

        print("YES")
        print(a, b, c)