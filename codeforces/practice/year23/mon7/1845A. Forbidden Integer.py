import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    if k == x == 1:
        print("NO")
    elif n % 2 == 1 and x == 1 and k < 3:
        print("NO")
    else:
        print("YES")
        if x != 1:
            print(n)
            print(*([1] * n))
        else:
            print(n // 2)
            if n % 2 == 0:
                print(*([2] * (n // 2)))
            else:
                print(*([2] * (n // 2 - 1) + [3]))

