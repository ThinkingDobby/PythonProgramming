import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())

    ans = 1
    for i in range(1, n + 1):
        if n % i != 0:
            break

        ans = i

    print(ans)