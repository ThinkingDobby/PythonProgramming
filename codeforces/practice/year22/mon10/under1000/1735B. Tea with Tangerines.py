import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    t = data[0] * 2 - 1
    s = 0
    for i in range(1, n):
        s += (data[i] + t - 1) // t - 1

    print(s)
