import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    if n >= 12:
        print("YES")
    elif n in [3, 6, 7, 9, 10]:
        print("YES")
    else:
        print("NO")