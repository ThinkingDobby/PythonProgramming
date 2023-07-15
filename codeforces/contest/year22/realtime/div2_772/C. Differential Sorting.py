import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if data[-2] > data[-1]:
        print(-1)
    else:
        midx = n - 2
        mv = data[-2]

        flag = True
        ans = []
        for i in range(n - 2, 0, -1):
            if data[i - 1] > data[i] and data[i] < mv - data[-1]:
                flag = False
                break
            else:
                if data[i - 1] < mv - data[-1]:
                    mv = data[i - 1]
                else:
                    ans.append((i, midx + 1, n))
                    mv -= data[-1]
                midx = i - 1

        if flag:
            print(len(ans))
            if len(ans) != 0:
                for i in ans:
                    print(*i)
        else:
            print(-1)
