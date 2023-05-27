import sys

input = sys.stdin.readline

chk = "codeforces"

for _ in range(int(input())):
    data = input().rstrip()
    cnt = 0
    for i in range(len(data)):
        if data[i] != chk[i]:
            cnt += 1

    print(cnt)