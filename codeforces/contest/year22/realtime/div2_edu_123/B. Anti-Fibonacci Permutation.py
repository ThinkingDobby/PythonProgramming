import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = sorted(range(1, n + 1), reverse=True)

    cnt = n - 1
    tmp = data[:]
    print(*tmp)
    for i in range(0, n, 2):
        if i + 1 < n:
            tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
            print(*tmp)
            cnt -= 1
            if cnt == 0:
                break

    if cnt != 0:
        tmp = data[:]
        for i in range(1, n, 2):
            if i + 1 < n:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                print(*tmp)
                cnt -= 1
                if cnt == 0:
                    break