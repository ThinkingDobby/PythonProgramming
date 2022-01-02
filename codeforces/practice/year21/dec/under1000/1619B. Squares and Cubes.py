memo = [i * i for i in range(1, 100000)]
memo += [i * i * i for i in range(1, 1001)]
memo = sorted(list(set(memo)))
for i in range(int(input())):
    tmp = int(input())
    cnt = 0
    for j in memo:
        if tmp < j: break
        cnt += 1
    print(cnt)
