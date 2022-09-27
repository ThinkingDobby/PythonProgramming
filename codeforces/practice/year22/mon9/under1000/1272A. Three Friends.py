import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))

    basic = b - a + c - a + c - b
    if a == b and b == c:
        print(0)
    else:
        print(max(0, basic - 4))
