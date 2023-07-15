# 미완성

for _ in range(int(input())):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    t = sorted(zip(b, c))
    print(t)

    prev = 1
    s = 0
    cost = 0
    for i in range(n):
        tmp = 0
        while prev < t[i][0] - 1:
            prev *= 2
            tmp += 1
        print(tmp, s + tmp)
        if s + tmp > k:
            break
        prev = t[i][0]
        s += tmp
        cost += t[i][1]

    print(cost)