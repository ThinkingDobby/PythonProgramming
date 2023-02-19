import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = data.count(2)

    if tmp % 2 == 1:
        print(-1)
    else:
        cnt = 0
        for i in range(n):
            if data[i] == 2:
                cnt += 1
            if cnt >= tmp // 2:
                print(i + 1)
                break
