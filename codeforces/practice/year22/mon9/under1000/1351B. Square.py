import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    print("YES" if max(a1, b1) == max(a2, b2) and min(a1, b1) + min(a2, b2) == max(a1, b1) else "NO")
