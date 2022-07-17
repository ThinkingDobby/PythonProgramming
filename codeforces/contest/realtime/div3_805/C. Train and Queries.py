import sys

input = sys.stdin.readline

for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    memo = dict()
    for i in range(n):
        x = str(data[i])
        if x in memo:
            memo[x][1] = i
        else:
            memo[x] = [i, i]

    for _ in range(k):
        a, b = map(int, input().split())
        x = str(a)
        y = str(b)
        if x in memo and y in memo and memo[x][0] < memo[y][1]:
            print("YES")
        else:
            print("NO")