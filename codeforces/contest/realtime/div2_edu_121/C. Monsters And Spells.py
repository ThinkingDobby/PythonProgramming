# 미완성

for _ in range(int(input())):
    n = int(input())
    k = [0] + list(map(int, input().split()))
    h = [0] + list(map(int, input().split()))

    tot = 0
    i = n
    while i >= 0:
        tmp = h[i]
        while k[i] - k[i - 1] > h[i] - h[i - 1] and i != 1:
            tmp = h[i - 1] + (k[i] - k[i - 1])
            i -= 1
            if i == 0:
                break
        ans = tmp * (tmp + 1) // 2
        print(ans)
        tot += ans
        i -= 1

    print(tot)
    # cnt = 0
    # last = 0
    # prev = 0
    # for i in range(1, n + 1):
    #     if k[i] - k[i - 1] >= h[i]:
    #         tmp = h[i] * (h[i] + 1) // 2
    #         prev = h[i]
    #         cnt += tmp
    #         last = tmp
    #     else:
    #         prev = prev + k[i] - k[i - 1]
    #         cnt += prev * (prev + 1) // 2 - last
    #         last = prev * (prev + 1) // 2
    #
    #
    # print(cnt)
