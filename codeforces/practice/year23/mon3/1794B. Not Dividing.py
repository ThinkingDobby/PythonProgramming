import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data = data

    for i in range(n):
        if data[i] == 1:
            data[i] += 1

    ans = [data[0]]
    for i in range(1, n):
        if data[i] % data[i - 1] == 0:
            data[i] += 1
        ans.append(data[i])

    print(*ans)