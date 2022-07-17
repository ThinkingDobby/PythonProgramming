import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    memo = [True for _ in range(n + 1)]

    memo[1] = False
    print(2)
    print(1, end=' ')
    for i in range(2, n + 1):
        if memo[i]:
            j = i
            while True:
                if j > n:
                    break
                if memo[j]:
                    memo[j] = False
                    print(j, end=' ')
                j *= 2

    print()

