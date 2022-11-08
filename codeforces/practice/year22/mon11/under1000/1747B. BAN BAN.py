import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    print((n + 1) // 2)

    for i in range((n + 1) // 2):
        print(3 * i + 1, 3 * (n - i))
