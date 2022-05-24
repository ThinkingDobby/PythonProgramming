import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = 'c' + input().rstrip() + 'c'

    flag = True
    for i in range(1, len(data) - 1):
        if data[i] != data[i - 1] and data[i] != data[i + 1]:
            flag = False
            break

    print("YES" if flag else "NO")
