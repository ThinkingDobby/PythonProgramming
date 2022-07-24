import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()
    tmp = set(input().split()[1:])

    memo = []
    cnt = 0
    prev = 0
    for i in range(n):
        if data[i] in tmp:
            memo.append(i - prev)
            prev = i

    print(max(memo) if memo else 0)
