import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print("NO")
    else:
        print("YES")
        if n % 2 == 0:
            print(*([1, -1] * (n // 2)))
        else:
            print(*([n // 2 - 1, -(n // 2)] * (n // 2) + [n // 2 - 1]))
