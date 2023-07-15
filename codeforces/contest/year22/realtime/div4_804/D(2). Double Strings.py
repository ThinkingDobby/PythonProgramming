import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [input().rstrip() for _ in range(n)]
    data_set = set(data)

    ans = set()
    for i in range(n):
        ans = False
        for j in range(1, len(data[i])):
            f = data[i][:j]
            s = data[i][j:]
            if f in data_set and s in data_set:
                print(1, end='')
                ans = True
                break
        if not ans:
            print(0, end='')
    print()
