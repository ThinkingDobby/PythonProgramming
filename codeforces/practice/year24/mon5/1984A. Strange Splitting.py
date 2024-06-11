import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if len(set(data)) == 1:
        print("NO")
    else:
        print("YES")
        if data[0] == data[1]:
            print('R' + 'B' * (n - 1))
        else:
            print('R' * (n - 1) + 'B')