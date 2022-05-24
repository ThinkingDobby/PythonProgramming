import math
import sys

input = sys.stdin.readline


def get_diff(a, b, m):
    return sum([abs(ord(a[i]) - ord(b[i])) for i in range(m)])


for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [input().rstrip() for _ in range(n)]
    mv = math.inf
    for i in range(n - 1):
        for j in range(i + 1, n):
            mv = min(mv, get_diff(data[i], data[j], m))

    print(mv)
