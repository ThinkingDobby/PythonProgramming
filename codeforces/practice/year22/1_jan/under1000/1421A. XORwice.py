import sys

inp = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, inp().split())
    print(a ^ b)
