for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    cnt = n // 2
    for i in range(1, n):
        print(data[i], data[0])
        cnt -= 1
        if cnt == 0:
            break
