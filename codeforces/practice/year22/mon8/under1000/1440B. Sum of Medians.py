import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    s = 0
    tmp = (n - 1) // 2
    for i in range(tmp * k, n * k, n - tmp):
        s += data[i]

    print(s)