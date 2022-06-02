import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    cnt = 0
    for i in range(n // 2 - 1, -1, -1):
        if data[i] != data[n // 2]:
            break
        cnt += 1
    for i in range(n // 2, n):
        if data[i] != data[n // 2]:
            break
        cnt += 1
    print(cnt)
