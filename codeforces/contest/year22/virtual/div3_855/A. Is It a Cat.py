import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip().lower() + '0'

    chk = "meow"
    now = 0

    ans = True
    for i in range(1, n + 1):
        if data[i - 1] != data[i]:
            if data[i - 1] == chk[now]:
                now += 1
                if now == 4:
                    if i != n:
                        ans = False
                    break
            else:
                ans = False

    print("YES" if ans and now == 4 else "NO")