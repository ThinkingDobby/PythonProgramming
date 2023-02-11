import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    x = 0
    y = 0

    chk = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}

    ans = False
    for i in range(n):
        tmp = chk[data[i]]
        x += tmp[0]
        y += tmp[1]

        if x == 1 and y == 1:
            ans = True
            break

    print("YES" if ans else "NO")