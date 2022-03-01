import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    memo = [chr(i) for i in range(97, 97 + k)]
    for i in range(n):
        print(memo[i % k], end='')
    print()
