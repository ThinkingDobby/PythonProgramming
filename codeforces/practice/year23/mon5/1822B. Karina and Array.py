import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    ans = max([data[0] * data[1], data[-1] * data[-2]])
    print(ans)
