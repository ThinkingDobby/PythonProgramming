import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    data = list(map(int, input().split()))
    print(k // 2 * 6)
    for i in range(k // 2):
        print(2, i + 1, i + k // 2 + 1)
        print(1, i + 1, i + k // 2 + 1)
        print(1, i + 1, i + k // 2 + 1)
        print(2, i + 1, i + k // 2 + 1)
        print(1, i + 1, i + k // 2 + 1)
        print(1, i + 1, i + k // 2 + 1)