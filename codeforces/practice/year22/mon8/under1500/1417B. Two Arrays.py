import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, t = map(int, input().split())
    data = list(map(int, input().split()))

    if t % 2 == 0:
        cnt = data.count(t // 2) // 2
        for i in data:
            if i > t // 2:
                print(1, end=' ')
            else:
                if i == t // 2 and cnt:
                    print(1, end=' ')
                    cnt -= 1
                else:
                    print(0, end=' ')
    else:
        for i in data:
            if i > t // 2:
                print(1, end=' ')
            else:
                print(0, end=' ')
    print()