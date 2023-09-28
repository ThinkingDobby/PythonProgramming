import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    ans = ((abs(a - b) + 1) // 2 + c - 1) // c
    print(ans)