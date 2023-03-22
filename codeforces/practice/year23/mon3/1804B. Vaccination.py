import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, d, w = map(int, input().split())
    data = list(map(int, input().split()))

    i = 0
    ans = 0
    while i < n:
        start = data[i] + w
        end = data[i] + w + d
        cnt = k
        ans += 1

        while data[i] <= end and cnt > 0:
            i += 1
            cnt -= 1

            if i >= n:
                break

    print(ans)

