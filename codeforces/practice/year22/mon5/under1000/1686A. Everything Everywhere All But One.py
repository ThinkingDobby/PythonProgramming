import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    s = sum(data)

    flag = False
    for i in data:
        if (s - i) == (n - 1) * i:
            flag = True
            break

    print("YES" if flag else "NO")