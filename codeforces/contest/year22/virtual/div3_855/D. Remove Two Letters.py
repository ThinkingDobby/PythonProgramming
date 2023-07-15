import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    cnt = 0

    for i in range(n - 2):
        if data[i] == data[i + 2]:
            cnt += 1

    print(n - 1 - cnt)