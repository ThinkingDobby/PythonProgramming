import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip())) + [2]

    chk = []
    flag = False
    for i in range(1, n + 1):
        if data[i - 1] != data[i]:
            if not flag:
                if data[i - 1] == 1:
                    flag = True
            else:
                chk.append(data[i - 1])

    print(len(chk))