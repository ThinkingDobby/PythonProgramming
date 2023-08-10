import sys

input = sys.stdin.readline


def gcd(a, b, cnt):
    if b == 0:
        return cnt
    else:
        return gcd(b, a % b, cnt + a // b)


for _ in range(int(input())):
    a, b = map(int, input().split())

    ans = gcd(max(a, b), min(a, b), 0)
    print(ans)
