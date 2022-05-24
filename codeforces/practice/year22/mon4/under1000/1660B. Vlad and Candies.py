import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    if n == 1:
        print("NO" if data[0] > 1 else "YES")
    else:
        print("NO" if abs(data[-1] - data[-2]) > 1 else "YES")
