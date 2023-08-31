import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    ans = [1]
    chk = {1}

    for i in range(2, n + 1):
        now = i
        while now <= n:
            if now not in chk:
                chk.add(now)
                ans.append(now)
            now *= 2

    print(*ans)