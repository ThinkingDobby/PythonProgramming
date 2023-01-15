import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = 1
    for i in data:
        tmp *= i
    print(((n - 1) + tmp) * 2022)