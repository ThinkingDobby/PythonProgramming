for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    flag = False
    idx = data.index(1)

    now = data[:]
    if idx != n - 1:
        now = data[idx + 1:] + data[:idx + 1]
    if now == sorted(data, reverse=True):
        flag = True

    now = data[:]
    if idx != 0:
        now = data[idx:] + data[:idx]
    if now == sorted(data):
        flag = True

    if flag:
        print("YES")
    else:
        print("NO")