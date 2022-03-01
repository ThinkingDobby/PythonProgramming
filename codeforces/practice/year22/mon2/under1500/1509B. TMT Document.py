import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    lim = data.count('M')

    cnt = 0
    cnt0 = 0

    mv = -1
    flag = True

    if lim * 2 != data.count('T'):
        flag = False
    else:
        for i in data:
            if i == 'T':
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0 or cnt > lim:
                flag = False
                break
            mv = max(cnt, mv)

    if flag:
        print("YES")
    else:
        print("NO")