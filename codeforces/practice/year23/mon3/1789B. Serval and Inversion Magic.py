import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, list(input().rstrip())))

    chk1 = False
    chk2 = False
    ans = True

    for i in range(n // 2):
        if data[i] != data[-(i + 1)] and not chk1:
            chk1 = True

        if data[i] == data[-(i + 1)] and chk1:
            chk2 = True

        if data[i] != data[-(i + 1)] and chk2:
            ans = False

    print("YES" if ans else "NO")