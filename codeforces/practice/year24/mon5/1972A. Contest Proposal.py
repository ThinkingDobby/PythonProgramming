import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = j = 0
    ans = cnt = 0
    while i < n and j < n:
        if a[i] > b[j]:
            j += 1
            cnt += 1
        else:
            ans += cnt
            cnt = 0
            i += 1
            j += 1

    ans += cnt
    print(ans)