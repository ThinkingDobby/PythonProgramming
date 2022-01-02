for t in range(int(input())):
    w, h = map(int, input().split(" "))
    m = -1
    for i in range(4):
        a = list(map(int, input().split(" ")))[1:]
        if i < 2: m = max(m, (max(a) - min(a)) * h)
        else: m = max(m, (max(a) - min(a)) * w)
    print(m)
