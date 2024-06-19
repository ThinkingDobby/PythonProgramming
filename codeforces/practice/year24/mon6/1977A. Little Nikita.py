import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    print("YES" if n >= m and (n - m) % 2 == 0 else "NO")