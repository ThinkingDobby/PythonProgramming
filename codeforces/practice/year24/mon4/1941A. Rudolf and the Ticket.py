import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    b = sorted(map(int, input().split()))
    c = sorted(map(int, input().split()))

    cnt = 0
    for i in b:
        for j in c:
            if i + j <= k:
                cnt += 1
            else:
                break

    print(cnt)