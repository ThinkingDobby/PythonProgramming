import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))
    memo = [0] * 102

    for i in data:
        memo[i] += 1

    f = -1
    s = -1
    sfin = False
    for i in range(102):
        if memo[i] > 1:
            f = i
            if not sfin:
                s = i
        elif memo[i] == 1:
            f = i
            sfin = True
        elif memo[i] == 0:
            break

    print(f + s + 2)
