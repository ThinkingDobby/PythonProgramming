import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = a.count(0)
    if cnt > (n + 1) // 2:
        tmp = a.count(1)
        if tmp != 0 and tmp + cnt == n:
            print(2)
        else:
            print(1)
    else:
        print(0)
