import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    memo = sorted(zip(a, b))

    print(*[i[0] for i in memo])
    print(*[i[1] for i in memo])