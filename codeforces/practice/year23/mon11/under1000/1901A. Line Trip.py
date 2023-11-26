import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    data = list(map(int, input().split()))

    data = [0] + data
    data += [x + x - i for i in data][::-1]

    ans = -1
    for i in range(1, len(data)):
        ans = max(ans, abs(data[i] - data[i - 1]))

    print(ans)