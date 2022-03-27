import sys

input = sys.stdin.readline

for _ in range(int(input())):
    q, d = map(int, input().split())
    data = list(map(int, input().split()))
    for now in data:
        if now >= d * 10:
            print("YES")
        else:
            tmp = now // 10 * 10 + d
            if now % 10 < d:
                tmp -= 10
            flag = False
            while tmp >= d:
                if (now - tmp) % d == 0:
                    flag = True
                    break
                tmp -= 10

            if flag:
                print("YES")
            else:
                print("NO")