import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()), reverse=True)

    if data[0] == data[1]:
        if data[0] == data[-1]:
            print("NO")
        else:
            print("YES")
            print(*([data[0], data[-1], data[1]] + data[2:-1]))
    else:
        print("YES")
        print(*data)