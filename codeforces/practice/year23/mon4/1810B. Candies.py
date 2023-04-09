import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 0:
        print(-1)
    else:
        tmp = str(bin(n))[2:]
        ans = []

        for i in range(len(tmp) - 1):
            ans.append(2 if tmp[i] == '1' else 1)
        print(len(ans))
        print(*ans)

