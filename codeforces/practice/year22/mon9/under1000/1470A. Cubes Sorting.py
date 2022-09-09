import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    if len(set(data)) == n and data == sorted(data)[::-1]:
        print("NO")
    else:
        print("YES")