import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    memo = sorted([[i, data[i] % k if data[i] % k != 0 else k] for i in range(n)], key=lambda x: (-x[1], x[0]))
    for i in memo:
        print(i[0] + 1, end=' ')
    print()
