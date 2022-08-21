import sys

input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())
    if n % 2 + m % 2 == 1:
        print("Burenka")
    else:
        print("Tonya")