import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    chk = len([i for i in data if i < 0])

    print(*([i for i in range(1, n - chk + 1)] + [i for i in range(n - chk - 1, n - chk - chk - 1, -1)]))
    print(*([1, 0] * chk + [i for i in range(1, n - chk * 2 + 1)]))