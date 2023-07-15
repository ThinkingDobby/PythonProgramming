import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if sum(data) == 0:
        s = 0
        ans = True
        chk = False
        for i in data:
            s += i
            if chk and i != 0:
                ans = False
                break
            if s <= 0:
                chk = True
        print("YES" if ans else "NO")
    else:
        print("NO")