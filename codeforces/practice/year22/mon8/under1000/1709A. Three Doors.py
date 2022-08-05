import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = data[n - 1]
    if tmp == 0 or data[tmp - 1] == 0:
        print("NO")
    else:
        print("YES")