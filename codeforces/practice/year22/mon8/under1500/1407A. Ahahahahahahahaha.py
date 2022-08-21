import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    zeros = data.count(0)

    if zeros >= n // 2:
        print(n // 2)
        print(*[0 for _ in range(n // 2)])
    else:
        if (n // 2) % 2 == 1:
            if zeros < n // 2:
                print(n // 2 + 1)
                print(*[1 for _ in range(n // 2 + 1)])
            else:
                tmp = 2
                chk = n // 2 - 1
                ans = []
        else:
            print(n // 2)
            print(*[1 for _ in range(n // 2)])