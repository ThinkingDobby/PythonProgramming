import sys

input = sys.stdin.readline


def fac(num):
    now = 1
    tmp = num
    while tmp > 0:
        now = (now * tmp) % 1000000007
        tmp -= 1

    return now


for _ in range(int(input())):
    n = int(input())

    ans = n * (n - 1) * fac(n) % 1000000007
    print(ans)
