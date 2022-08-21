import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(range(1, n + 1))

    print(n)
    print(*data)
    for i in range(1, n):
        data[i - 1], data[i] = data[i], data[i - 1]
        print(*data)