import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip()))
    if n == 2 and data[0] >= data[1]:
        print("NO")
    else:
        print("YES")
        print(2)
        print(data[0], ''.join(map(str, data[1:])))