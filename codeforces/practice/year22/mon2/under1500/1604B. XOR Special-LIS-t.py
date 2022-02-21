import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n % 2 == 0:
        print("YES")
    else:
        flag = False
        for i in range(1, n):
            if data[i - 1] >= data[i]:
                flag = True
                break
        if not flag:
            print("NO")
        else:
            print("YES")
