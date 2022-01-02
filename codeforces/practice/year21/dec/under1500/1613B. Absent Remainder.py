from collections import Counter

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    d = Counter(data)

    cnt = n // 2
    flag = False
    for i in range(n):
        for j in range(i):
            if d[data[i] % data[j]] == 0:
                print(data[i], data[j])
                cnt -= 1
                if cnt == 0:
                    flag = True
                    break
        if flag:
            break
