import sys

input = sys.stdin.readline

for _ in range(int(input())):
    chk = dict()
    n = int(input())
    data = input().rstrip()

    ans = True
    for i in range(n):
        if data[i] in chk:
            if chk[data[i]] != i % 2:
                ans = False
                break
        else:
            chk[data[i]] = i % 2

    print("YES" if ans else "NO")