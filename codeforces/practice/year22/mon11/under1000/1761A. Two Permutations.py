import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    print("YES" if n - 1 > a + b or n == a == b else "NO")

