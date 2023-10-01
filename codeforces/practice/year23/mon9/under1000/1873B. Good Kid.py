import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(map(int, input().split()))

    tmp = 1
    for i in range(1, n):
        tmp *= data[i]
    ans = (data[0] + 1) * tmp
    print(ans)