n, a, b = map(int, input().split())

if n > a * b:
    print(-1)
else:
    now = 1
    flag = False
    for i in range(a):
        ans = []
        for _ in range(b):
            if i % 2 == 0:
                ans.append(now)
            else:
                ans.insert(0, now)
            if not flag:
                now += 1
            if now > n:
                now = 0
                flag = True
        print(*ans)