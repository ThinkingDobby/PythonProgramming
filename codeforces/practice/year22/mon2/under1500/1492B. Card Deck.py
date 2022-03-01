import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = [-1] + list(map(int, input().split()))
    memo = [False] * (n + 1)

    end = n + 1
    mv = n
    for i in range(n, -1, -1):
        if data[i] == mv:
            for j in range(i, end):
                print(data[j], end=' ')
                memo[data[j]] = True
            end = i
            mv -= 1
            while memo[mv]:
                mv -= 1
    print()