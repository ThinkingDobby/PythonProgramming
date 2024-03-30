import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1:
        print("NO")
    else:
        print("YES")
        for i in range(n // 2):
            if i % 2 == 0:
                print("AA", end='')
            else:
                print("BB", end='')
        print()