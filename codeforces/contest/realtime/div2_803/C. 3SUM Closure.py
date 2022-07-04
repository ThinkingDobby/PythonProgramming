import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    if n == 3:
        print("YES" if sum(data) in data else "NO")
    elif n == 4:
        ans = True
        for i in range(4):
            if (sum(data) - data[i]) not in data:
                ans = False
        print("YES" if ans else "NO")
    else:
        tmp = set(data)
        if len(tmp) == 1 and data[0] == 0:
            print("YES")
        else:
            ncnt = 0
            pcnt = 0
            nmemo = []
            pmemo = []
            ans = True
            for i in data:
                if i < 0:
                    ncnt += 1
                    nmemo.append(i)
                elif i > 0:
                    pcnt += 1
                    pmemo.append(i)
                if pcnt > 2 or ncnt > 2:
                    ans = False
                    break

            if not ans:
                print("NO")
            else:
                tmp = nmemo + pmemo
                zcnt = data.count(0)
                if zcnt > 1:
                    tmp.append(0)
                    tmp.append(0)
                elif zcnt == 2:
                    tmp.append(0)

                ans = True
                for t1 in range(len(tmp) - 2):
                    for t2 in range(t1 + 1, len(tmp) - 1):
                        for t3 in range(t2 + 1, len(tmp)):
                            if (tmp[t1] + tmp[t2] + tmp[t3]) not in tmp:
                                ans = False
                                break

                print("YES" if ans else "NO")

