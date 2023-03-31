import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    tmp = data[0]
    chk = [[0, 0]] * n
    for i in range(n):
        tmp = math.gcd(tmp, data[i])

    if tmp == 1:
        print(0)
    else:
        ans = -1

        for i in range(n):
            chk[i] = [math.gcd(data[i], i + 1), n - i]

        for i in range(n - 1, -1, -1):
            if math.gcd(tmp, chk[i][0]) == 1:
                ans = chk[i][1]
                break

        memo = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if math.gcd(chk[i][0], math.gcd(tmp, chk[j][0])) == 1:
                    ans = min(ans, chk[i][1] + chk[j][1])

        print(ans)
