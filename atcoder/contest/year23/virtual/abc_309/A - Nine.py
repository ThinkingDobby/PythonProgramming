import sys

input = sys.stdin.readline

a, b = map(int, input().split())
print("Yes" if ((a + 2) // 3 == (b + 2) // 3) and (b - a == 1) else "No")