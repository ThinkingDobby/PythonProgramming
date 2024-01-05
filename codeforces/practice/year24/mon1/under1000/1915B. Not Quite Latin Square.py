import sys

input = sys.stdin.readline

memo = {'A', 'B', 'C'}

for _ in range(int(input())):
    data = [input().rstrip() for _ in range(3)]

    for i in range(3):
        for j in range(3):
            if data[i][j] == '?':
                ans = list(memo - set(data[i]))[0]
                break

    print(ans)
