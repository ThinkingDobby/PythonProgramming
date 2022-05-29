import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    if max(a) > max(b):
        print("Alice")
        print("Alice")
    elif max(a) < max(b):
        print("Bob")
        print("Bob")
    else:
        print("Alice")
        print("Bob")
