import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [input().rstrip() for _ in range(n)]

    mv = -1
    mr = -1
    ans = True
    for i in range(n):
        if 'R' in data[i] and mv == -1:
            mv = i
            mr = data[i].find('R')
        else:
            tmp = data[i].find('R')
            if tmp < mr and tmp != -1:
                ans = False
                break

    print("YES" if ans else "NO")