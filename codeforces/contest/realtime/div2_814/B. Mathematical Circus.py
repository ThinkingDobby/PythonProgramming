import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    if k % 2 == 1:
        if (1 + k) % 2 != 0:
            print("NO")
        else:
            print("YES")
            for i in range(0, n, 2):
                print(i + 1, i + 2)
    else:
        if (2 + k) % 4 != 0:
            print("NO")
        else:
            print("YES")
            tog = False
            for i in range(0, n, 2):
                if tog:
                    print(i + 1, i + 2)
                    tog = False
                else:
                    print(i + 2, i + 1)
                    tog = True
