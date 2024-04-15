import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, m = map(int, input().split())

    print(m // a + m // b + 2)