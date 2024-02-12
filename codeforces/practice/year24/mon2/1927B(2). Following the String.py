import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    memo = [0] * 26

    ans = ''
    for i in range(n):
        for j in range(26):
            if data[i] == memo[j]:
                ans += chr(97 + j)
                memo[j] += 1
                break

    print(ans)