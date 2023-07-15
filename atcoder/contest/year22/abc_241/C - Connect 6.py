import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

flag = False
for i in range(n):
    for j in range(n):
        if j + 5 < n:
            if data[i][j:j + 6].count('#') >= 4:
                flag = True
                break

        if i + 5 < n:
            cnt = 0
            for k in range(6):
                if data[i + k][j] == '#':
                    cnt += 1
            if cnt >= 4:
                flag = True
                break

        if i + 5 < n and j + 5 < n:
            cnt = 0
            for k in range(6):
                if data[i + k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                flag = True
                break

        if i + 5 < n and j + 5 < n:
            cnt = 0
            for k in range(6):
                if data[i + 5 - k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                flag = True
                break

    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
