import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = [data[0]]
    for i in range(1, n):
        if data[i - 1] > data[i]:
            ans.append(data[i])
            ans.append(data[i])
        else:
            ans.append(data[i])

    print(len(ans))
    print(*ans)