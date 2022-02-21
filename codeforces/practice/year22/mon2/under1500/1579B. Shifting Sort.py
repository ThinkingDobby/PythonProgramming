import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    now = [data[0]]
    ans = []

    for i in range(1, n):
        cnt = 0
        for j in range(i - 1, -1, -1):
            if now[j] > data[i]:
                cnt += 1
            else:
                break
        now.insert(i - cnt, data[i])
        if cnt:
            ans.append([i - cnt + 1, i + 1, cnt])

    print(len(ans))
    if len(ans):
        for i in ans:
            print(*i)
