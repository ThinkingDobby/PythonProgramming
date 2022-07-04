import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n % 2 == 0:
        print("Joe" if data.index(min(data)) % 2 == 0 else "Mike")
    else:
        print("Mike")
