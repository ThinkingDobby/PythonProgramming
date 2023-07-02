import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sum(map(int, input().split()))
    b = sum(map(int, input().split()))

    if a == b:
        print("Draw")
    else:
        print("Tsondu" if a > b else "Tenzing")
