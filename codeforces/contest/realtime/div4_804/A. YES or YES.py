import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = input().rstrip().lower()
    if data == "yes":
        print("YES")
    else:
        print("NO")