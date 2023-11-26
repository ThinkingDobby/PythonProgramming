import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    ans = [2 * i + 1 for i in range(n)]
    print(*ans)
