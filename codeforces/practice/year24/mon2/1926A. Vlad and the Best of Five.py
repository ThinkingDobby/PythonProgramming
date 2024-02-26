import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip()

    cnt = data.count('A')

    print("A" if cnt > 2 else "B")