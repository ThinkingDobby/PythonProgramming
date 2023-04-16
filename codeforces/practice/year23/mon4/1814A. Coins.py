import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    print("YES" if n % 2 == 0 or (n % 2 == 1 and k % 2 == 1) else "NO")