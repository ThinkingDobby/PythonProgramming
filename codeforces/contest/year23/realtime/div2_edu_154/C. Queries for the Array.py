# WA

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    data = list(input().rstrip())
    memo = [i for i in data if i != '+' and i != '-']
    if len(memo) == 0:
        print("YES")
    else:
        memo = [memo[0]] + memo

        mi = 0
        cnt = 0
        ans = True
        chk = False
        for i in range(len(data)):
            if data[i] == '+':
                cnt += 1
            elif data[i] == '-':
                cnt -= 1

            if memo[mi] != memo[mi + 1] and cnt <= 1:
                chk = True

            if data[i] == '0' or data[i] == '1':
                if memo[mi] != memo[mi + 1]:
                    if not chk:
                        ans = False
                        break

                if memo[mi + 1] == '0' and cnt <= 1:
                    ans = False
                    break

                mi += 1
                if mi >= len(memo) - 1:
                    break

                if memo[mi] != memo[mi + 1]:
                    chk = cnt <= 1

        print("YES" if ans else "NO")


