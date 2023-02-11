import sys

input = sys.stdin.readline

chk = "314159265358979323846264338327"

for _ in range(int(input())):
    data = input().rstrip()

    ans = -1
    for i in range(len(data)):
        if data[i] != chk[i]:
            break
        ans = i

    print(ans + 1)