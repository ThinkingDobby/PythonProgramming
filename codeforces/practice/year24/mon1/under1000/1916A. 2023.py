import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    now = data[0]
    for i in range(1, n):
        now *= data[i]

    if 2023 % now != 0:
        print("NO")
    else:
        print("YES")
        print(*([2023 // now] + [1] * (k - 1)))

