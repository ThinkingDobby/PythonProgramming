import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if sum(data) == 0:
        print("NO")
    elif sum(data) < 0:
        print("YES")
        print(*sorted(data))
    else:
        print("YES")
        print(*sorted(data, reverse=True))
