import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(map(int, input().split()))

    ans = [0] * 3
    for i in range(3):
        if (sum(data) - data[i]) % 2 == 0:
            ans[i] = 1

    print(*ans)
