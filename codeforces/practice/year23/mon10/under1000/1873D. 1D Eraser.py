import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(input().rstrip())

    i = 0
    cnt = 0
    while i < n:
        if data[i] == 'B':
           cnt += 1
           i += k
           continue

        i += 1

    print(cnt)
