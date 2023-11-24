import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    chk = False
    print("First" if (n + 1) % 3 == 0 or (n - 1) % 3 == 0 else "Second")