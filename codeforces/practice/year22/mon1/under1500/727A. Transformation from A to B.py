import heapq

a, b = map(int, input().split())

flag = True
tmp = b
cnt = 0
ans = [b]
while True:
    if tmp % 10 == 1:
        tmp = tmp // 10
    elif tmp % 2 == 0:
        tmp //= 2
    elif tmp != a:
        flag = False
        break

    cnt += 1
    heapq.heappush(ans, tmp)
    if tmp == a:
        break
    if tmp < a:
        flag = False
        break

if flag:
    print("YES")
    print(len(ans))
    while ans:
        print(heapq.heappop(ans), end=' ')
    print()
else:
    print("NO")