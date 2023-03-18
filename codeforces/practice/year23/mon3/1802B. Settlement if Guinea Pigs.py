import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    m = data.count(1)
    f = data.count(2)

    print(m // 2 + f // 2 + m % 2 + f % 2)