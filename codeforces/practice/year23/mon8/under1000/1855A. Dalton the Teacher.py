import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(lambda x: int(x) - 1, input().split()))

    cnt = 0
    for i in range(n):
        if i == data[i]:
            cnt += 1

    print((cnt + 1) // 2)