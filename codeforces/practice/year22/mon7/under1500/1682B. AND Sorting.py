import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    ans = -1
    for i in range(n):
        if data[i] != i:
            if ans == -1:
                ans = data[i]
            else:
                ans &= data[i]

    print(ans)