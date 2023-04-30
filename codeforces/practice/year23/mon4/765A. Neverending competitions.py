import sys

input = sys.stdin.readline

n = int(input())
depart = input().rstrip()
data = [input().rstrip() for _ in range(n)]

print("home" if n % 2 == 0 else "contest")