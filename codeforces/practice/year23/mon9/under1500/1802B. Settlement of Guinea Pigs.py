import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    k_cnt = uk_cnt = 0
    tmp = 0
    ans = 0
    for i in range(n):
        if data[i] == 1:
            uk_cnt += 1

        ans = max(ans, uk_cnt + tmp)

        if data[i] == 2:
            k_cnt += uk_cnt

            if k_cnt > 1:
                tmp = (k_cnt - 2) // 2 + 2
            else:
                tmp = k_cnt

            uk_cnt = 0

    print(ans)

