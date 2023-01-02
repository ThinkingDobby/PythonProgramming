import sys

input = sys.stdin.readline

for _ in range(int(input())):
    input()
    data = [list(map(int, input().split())) for _ in range(3)]
    if (data[0][0] == data[1][0] or data[0][0] == data[2][0] or data[1][0] == data[2][0]) \
            and (data[0][1] == data[1][1] or data[0][1] == data[2][1] or data[1][1] == data[2][1]):
        print("NO")
    else:
        print("YES")
