import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print("Bob" if n <= 4 else "Alice")