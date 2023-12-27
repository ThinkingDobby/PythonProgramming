import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    now = data[0]
    chk = {data[0]}

    ans = True
    for i in range(1, n):
        if now >= data[i]:
            chk.add(now)
            now = data[i]
        else:
            if now in chk:
                ans = False
                break

    print("NO" if ans else "YES")