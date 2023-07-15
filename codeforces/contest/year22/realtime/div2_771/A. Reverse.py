for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    idx = 0
    tv = 1
    for i in range(n):
        if i + 1 != data[i]:
            idx = i
            tv = i + 1
            break
    tmp = data.index(tv)
    print(*(data[:idx] + data[idx:tmp + 1][::-1] + data[tmp + 1:]))