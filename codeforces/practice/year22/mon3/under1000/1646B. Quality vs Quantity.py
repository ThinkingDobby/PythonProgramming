import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    f = data[0]
    b = 0
    flag = False
    for i in range(1, n):
        if 2 * i + 1 > n:
            break
        f += data[i]
        b += data[-i]
        if f < b:
            flag = True
            break

    print("YES" if flag else "NO")
