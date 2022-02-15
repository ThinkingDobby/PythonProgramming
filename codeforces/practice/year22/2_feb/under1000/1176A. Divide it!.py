import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    cnt2 = 0
    cnt3 = 0
    cnt5 = 0

    while n > 1:
        while n % 2 == 0:
            n //= 2
            cnt2 += 1
        while n % 3 == 0:
            n //= 3
            cnt3 += 1
        while n % 5 == 0:
            n //= 5
            cnt5 += 1
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
            break

    if n == 1:
        print(cnt2 + cnt3 * 2 + cnt5 * 3)
    else:
        print(-1)