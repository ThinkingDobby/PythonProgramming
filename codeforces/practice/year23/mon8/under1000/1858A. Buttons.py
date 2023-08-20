import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ta = (c + 1) // 2 + a
    tb = c // 2 + b

    print("First" if ta > tb else "Second")