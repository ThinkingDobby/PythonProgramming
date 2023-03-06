import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    odds = []
    evens = []

    for i in range(n):
        if data[i] % 2 == 1:
            odds.append(i + 1)
        else:
            evens.append(i + 1)

    if len(odds) >= 1 and len(evens) >= 2:
        print("YES")
        print(odds[0], *evens[:2])
    elif len(odds) >= 3:
        print("YES")
        print(*odds[:3])
    else:
        print("NO")

