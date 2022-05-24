import sys

input = sys.stdin.readline

memo = []

for _ in range(int(input())):
    data = input().rstrip()
    if data in memo:
        print("YES")
    else:
        print("NO")
        memo.append(data)