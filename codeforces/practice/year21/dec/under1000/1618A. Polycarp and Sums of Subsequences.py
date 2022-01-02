for t in range(int(input())):
    a = list(map(int, input().split(" ")))
    l = len(a)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                if a[i] + a[j] + a[k] == max(a):
                    print(a[i], a[j], a[k])
                    break
