import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    ans = []
    chk = set()
    now = 1
    for i in range(m):
        if data[i] not in chk:
            ans.append(now)
            chk.add(data[i])
        now += 1

    print(*([-1] * (n - len(ans)) + ans[:n][::-1]))
