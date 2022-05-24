import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(b * 2 + a + 1 if a != 0 else 1)