import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(k):
        if data[i] > k:
            cnt += 1

    print(cnt)